#!/usr/bin/env python3
"""
TrueCharts Application Version Cleanup Script

This script cleans up old application versions in a TrueCharts-style repository,
keeping only the 3 most recent versions for each application.
Handles both direct version directories and charts/ subdirectories.
"""

import os
import json
import shutil
from pathlib import Path
from typing import List, Tuple, Dict, Any
import logging
from packaging import version

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def parse_version(version_string: str) -> Tuple[version.Version, str]:
    """Parse a version string and return a Version object for sorting."""
    try:
        cleaned_version = version_string.strip()
        parsed_version = version.parse(cleaned_version)
        return (parsed_version, version_string)
    except version.InvalidVersion:
        try:
            import re
            numbers = re.findall(r'\d+', version_string)
            if len(numbers) >= 2:
                if len(numbers) >= 3:
                    fallback_version = f"{numbers[0]}.{numbers[1]}.{numbers[2]}"
                else:
                    fallback_version = f"{numbers[0]}.{numbers[1]}.0"

                parsed_version = version.parse(fallback_version)
                logger.warning(f"Using fallback version parsing for '{version_string}' -> '{fallback_version}'")
                return (parsed_version, version_string)
        except:
            pass

        logger.warning(f"Could not parse version: {version_string}, treating as 0.0.0")
        return (version.parse("0.0.0"), version_string)


def get_latest_versions(versions: List[str], keep_count: int = 3) -> List[str]:
    """Get the latest N versions from a list of version strings."""
    if not versions:
        return []

    logger.debug(f"Input versions: {versions}")

    # Parse versions and sort by version number (newest first)
    parsed_versions = [parse_version(v) for v in versions]

    # Sort by version (newest first)
    sorted_versions = sorted(parsed_versions, key=lambda x: x[0], reverse=True)

    # Return the latest N versions
    result = [v[1] for v in sorted_versions[:keep_count]]
    logger.debug(f"Keeping latest {keep_count} versions: {result}")

    return result


def get_version_directories(app_path: Path) -> Tuple[List[str], Path]:
    """
    Get all version directories from an application directory.
    Returns both the version list and the actual directory containing them.
    """
    version_dirs = []

    if not app_path.exists() or not app_path.is_dir():
        logger.warning(f"Application path does not exist: {app_path}")
        return version_dirs, app_path

    # Check for charts subdirectory first (common in TrueNAS/TrueCharts)
    charts_dir = app_path / "charts"
    search_dir = charts_dir if charts_dir.exists() else app_path

    logger.debug(f"Searching for versions in: {search_dir}")

    # Get all subdirectories that look like version numbers
    for item in search_dir.iterdir():
        if item.is_dir() and item.name not in ['charts', '.git', '__pycache__']:
            # Check if directory name looks like a version
            if any(char.isdigit() for char in item.name):
                version_dirs.append(item.name)

    return version_dirs, search_dir


def cleanup_version_directories(app_path: Path, keep_versions: List[str], dry_run: bool = False) -> List[str]:
    """Remove old version directories, keeping only the specified versions."""
    removed_dirs = []

    version_dirs, search_dir = get_version_directories(app_path)

    if not version_dirs:
        return removed_dirs

    logger.debug(f"Processing version directories in: {search_dir}")

    # Get actual directory objects for removal
    actual_dirs = []
    for item in search_dir.iterdir():
        if item.is_dir() and item.name in version_dirs:
            actual_dirs.append(item)

    # Remove directories for versions not in keep_versions
    for version_dir in actual_dirs:
        if version_dir.name not in keep_versions:
            if dry_run:
                logger.info(f"[DRY RUN] Would remove version directory: {version_dir}")
                removed_dirs.append(version_dir.name)
            else:
                try:
                    shutil.rmtree(version_dir)
                    removed_dirs.append(version_dir.name)
                    logger.info(f"Removed version directory: {version_dir}")
                except Exception as e:
                    logger.error(f"Failed to remove directory {version_dir}: {e}")

    return removed_dirs


def cleanup_application(app_path: Path, keep_count: int = 3, dry_run: bool = False, update_json: bool = True) -> Dict[str, Any]:
    """Clean up an individual application directory."""
    app_name = app_path.name
    action = "Analyzing" if dry_run else "Processing"
    logger.info(f"{action} application: {app_name}")

    result = {
        'app_name': app_name,
        'success': False,
        'kept_versions': [],
        'removed_directories': [],
        'removed_json_entries': [],
        'json_updated': False,
        'source': 'unknown'
    }

    try:
        # Get versions from directories (handles charts/ subdirectory)
        available_versions, search_dir = get_version_directories(app_path)
        result['source'] = 'directories'

        if not available_versions:
            logger.warning(f"No versions found for {app_name}")
            return result

        logger.info(f"Found versions in {search_dir.relative_to(app_path.parent) if search_dir != app_path else app_path.name}: {sorted(available_versions)}")

        # Get the latest versions to keep
        keep_versions = get_latest_versions(available_versions, keep_count)
        result['kept_versions'] = keep_versions

        action_verb = "Would keep" if dry_run else "Keeping"
        logger.info(f"{action_verb} versions: {keep_versions}")

        # Clean up version directories
        removed_dirs = cleanup_version_directories(app_path, keep_versions, dry_run)
        result['removed_directories'] = removed_dirs

        # Calculate removed entries
        result['removed_json_entries'] = [v for v in available_versions if v not in keep_versions]

        result['success'] = True

    except Exception as e:
        action_verb = "analyze" if dry_run else "process"
        logger.error(f"Failed to {action_verb} application {app_name}: {e}")

    return result


def cleanup_repository(base_path: str, keep_count: int = 3, dry_run: bool = False, update_json: bool = True, debug: bool = False) -> Dict[str, List[Dict[str, Any]]]:
    """Clean up all applications in a repository directory."""
    if debug:
        logger.setLevel(logging.DEBUG)

    base_dir = Path(base_path)

    if not base_dir.exists() or not base_dir.is_dir():
        logger.error(f"Base directory does not exist: {base_path}")
        return {'successful': [], 'failed': []}

    action = "Starting dry run analysis" if dry_run else "Starting cleanup"
    logger.info(f"{action} of repository: {base_path}")
    logger.info(f"{'Would keep' if dry_run else 'Keeping'} {keep_count} versions per application")

    if not update_json:
        logger.info("JSON file updates are DISABLED - will process directories only")

    if dry_run:
        logger.info("="*50)
        logger.info("DRY RUN MODE - NO FILES WILL BE MODIFIED")
        logger.info("="*50)

    results = {'successful': [], 'failed': []}

    # Process each application directory
    for item in base_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            result = cleanup_application(item, keep_count, dry_run, update_json)

            if result['success']:
                results['successful'].append(result)
            else:
                results['failed'].append(result)

    # Print summary
    logger.info("\n" + "="*50)
    summary_title = "DRY RUN SUMMARY" if dry_run else "CLEANUP SUMMARY"
    logger.info(summary_title)
    logger.info("="*50)
    logger.info(f"Successfully {'analyzed' if dry_run else 'processed'}: {len(results['successful'])} applications")
    logger.info(f"Failed to {'analyze' if dry_run else 'process'}: {len(results['failed'])} applications")

    if results['successful']:
        action_verb = "Would be cleaned" if dry_run else "Successful cleanups"
        logger.info(f"\n{action_verb}:")
        for result in results['successful']:
            verb = "would keep" if dry_run else "kept"
            verb2 = "would remove" if dry_run else "removed"

            logger.info(f"  {result['app_name']}: {verb} {len(result['kept_versions'])} versions, "
                       f"{verb2} {len(result['removed_directories'])} directories")

    if results['failed']:
        action_verb = "Failed to analyze" if dry_run else "Failed cleanups"
        logger.info(f"\n{action_verb}:")
        for result in results['failed']:
            logger.info(f"  {result['app_name']}: failed to process")

    return results


def main():
    """Main function to run the cleanup script."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Clean up old TrueCharts application versions"
    )
    parser.add_argument(
        "directory",
        help="Base directory to scan (e.g., '/stable/' or './stable')"
    )
    parser.add_argument(
        "--keep",
        type=int,
        default=3,
        help="Number of versions to keep per application (default: 3)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually deleting anything"
    )
    parser.add_argument(
        "--no-json-update",
        action="store_true",
        help="Skip updating app_versions.json files (only remove directories)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging to troubleshoot version parsing"
    )

    args = parser.parse_args()

    try:
        results = cleanup_repository(
            args.directory,
            args.keep,
            args.dry_run,
            update_json=not args.no_json_update,
            debug=args.debug
        )

        if args.dry_run:
            logger.info("\nDry run completed. Use without --dry-run to perform actual cleanup.")

        if args.no_json_update:
            logger.info("Note: JSON files were not modified due to --no-json-update flag")

        if results['failed']:
            exit(1)
        else:
            action = "analyzed" if args.dry_run else "processed"
            logger.info(f"All applications {action} successfully!")

    except KeyboardInterrupt:
        logger.info("Operation interrupted by user")
        exit(130)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        exit(1)


if __name__ == "__main__":
    main()

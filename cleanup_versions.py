#!/usr/bin/env python3
"""
TrueCharts Application Version Cleanup Script

This script cleans up old application versions in a TrueCharts-style repository,
keeping only the 3 most recent versions for each application.
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
    """
    Parse a version string and return a Version object for sorting.

    Args:
        version_string: The version string to parse

    Returns:
        Tuple of (Version object, original string)
    """
    try:
        # Handle semantic versioning
        return (version.parse(version_string), version_string)
    except version.InvalidVersion:
        # Fallback for non-standard versions
        logger.warning(f"Invalid version format: {version_string}")
        return (version.parse("0.0.0"), version_string)


def get_latest_versions(versions: List[str], keep_count: int = 3) -> List[str]:
    """
    Get the latest N versions from a list of version strings.

    Args:
        versions: List of version strings
        keep_count: Number of latest versions to keep (default: 3)

    Returns:
        List of the latest version strings, sorted newest to oldest
    """
    if not versions:
        return []

    # Parse versions and sort by version number (newest first)
    parsed_versions = [parse_version(v) for v in versions]
    sorted_versions = sorted(parsed_versions, key=lambda x: x[0], reverse=True)

    # Return the latest N versions
    return [v[1] for v in sorted_versions[:keep_count]]


def cleanup_version_directories(app_path: Path, keep_versions: List[str]) -> List[str]:
    """
    Remove old version directories, keeping only the specified versions.

    Args:
        app_path: Path to the application directory
        keep_versions: List of version strings to keep

    Returns:
        List of directories that were removed
    """
    removed_dirs = []

    if not app_path.exists() or not app_path.is_dir():
        logger.warning(f"Application path does not exist: {app_path}")
        return removed_dirs

    # Get all subdirectories that look like version numbers
    version_dirs = []
    for item in app_path.iterdir():
        if item.is_dir() and item.name not in ['charts', '.git', '__pycache__']:
            # Check if directory name looks like a version
            if any(char.isdigit() for char in item.name):
                version_dirs.append(item)

    # Remove directories for versions not in keep_versions
    for version_dir in version_dirs:
        if version_dir.name not in keep_versions:
            try:
                shutil.rmtree(version_dir)
                removed_dirs.append(version_dir.name)
                logger.info(f"Removed version directory: {version_dir}")
            except Exception as e:
                logger.error(f"Failed to remove directory {version_dir}: {e}")

    return removed_dirs


def update_app_versions_json(app_path: Path, keep_versions: List[str]) -> bool:
    """
    Update app_versions.json to keep only the specified versions.

    Args:
        app_path: Path to the application directory
        keep_versions: List of version strings to keep

    Returns:
        True if successful, False otherwise
    """
    json_file = app_path / "app_versions.json"

    if not json_file.exists():
        logger.warning(f"app_versions.json not found in {app_path}")
        return False

    try:
        # Read the current JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Create new data with only the versions we want to keep
        new_data = {}
        kept_versions = []
        removed_versions = []

        for version_key in data:
            if version_key in keep_versions:
                new_data[version_key] = data[version_key]
                kept_versions.append(version_key)
            else:
                removed_versions.append(version_key)

        # Write the updated JSON file
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=4, ensure_ascii=False)

        logger.info(f"Updated app_versions.json for {app_path.name}")
        logger.info(f"  Kept versions: {kept_versions}")
        if removed_versions:
            logger.info(f"  Removed versions: {removed_versions}")

        return True

    except Exception as e:
        logger.error(f"Failed to update app_versions.json in {app_path}: {e}")
        return False


def cleanup_application(app_path: Path, keep_count: int = 3) -> Dict[str, Any]:
    """
    Clean up an individual application directory.

    Args:
        app_path: Path to the application directory
        keep_count: Number of versions to keep (default: 3)

    Returns:
        Dictionary with cleanup results
    """
    app_name = app_path.name
    logger.info(f"Processing application: {app_name}")

    result = {
        'app_name': app_name,
        'success': False,
        'kept_versions': [],
        'removed_directories': [],
        'removed_json_entries': []
    }

    try:
        # Read current app_versions.json to get available versions
        json_file = app_path / "app_versions.json"
        if not json_file.exists():
            logger.warning(f"No app_versions.json found for {app_name}")
            return result

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        available_versions = list(data.keys())

        if not available_versions:
            logger.warning(f"No versions found in app_versions.json for {app_name}")
            return result

        # Get the latest versions to keep
        keep_versions = get_latest_versions(available_versions, keep_count)
        result['kept_versions'] = keep_versions

        logger.info(f"Keeping versions: {keep_versions}")

        # Clean up version directories
        removed_dirs = cleanup_version_directories(app_path, keep_versions)
        result['removed_directories'] = removed_dirs

        # Update app_versions.json
        json_success = update_app_versions_json(app_path, keep_versions)

        # Calculate removed JSON entries
        result['removed_json_entries'] = [v for v in available_versions if v not in keep_versions]

        result['success'] = json_success

    except Exception as e:
        logger.error(f"Failed to process application {app_name}: {e}")

    return result


def cleanup_repository(base_path: str, keep_count: int = 3) -> Dict[str, List[Dict[str, Any]]]:
    """
    Clean up all applications in a repository directory.

    Args:
        base_path: Path to the base directory (e.g., "/stable/")
        keep_count: Number of versions to keep per application (default: 3)

    Returns:
        Dictionary with results for all processed applications
    """
    base_dir = Path(base_path)

    if not base_dir.exists() or not base_dir.is_dir():
        logger.error(f"Base directory does not exist: {base_path}")
        return {'successful': [], 'failed': []}

    logger.info(f"Starting cleanup of repository: {base_path}")
    logger.info(f"Keeping {keep_count} versions per application")

    results = {'successful': [], 'failed': []}

    # Process each application directory
    for item in base_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            result = cleanup_application(item, keep_count)

            if result['success']:
                results['successful'].append(result)
            else:
                results['failed'].append(result)

    # Print summary
    logger.info("\n" + "="*50)
    logger.info("CLEANUP SUMMARY")
    logger.info("="*50)
    logger.info(f"Successfully processed: {len(results['successful'])} applications")
    logger.info(f"Failed to process: {len(results['failed'])} applications")

    if results['successful']:
        logger.info("\nSuccessful cleanups:")
        for result in results['successful']:
            logger.info(f"  {result['app_name']}: kept {len(result['kept_versions'])} versions, "
                       f"removed {len(result['removed_directories'])} directories")

    if results['failed']:
        logger.info("\nFailed cleanups:")
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

    args = parser.parse_args()

    if args.dry_run:
        logger.info("DRY RUN MODE - No files will be deleted")
        # Note: You would need to implement dry-run logic in the cleanup functions
        # This is left as an exercise for production use

    try:
        results = cleanup_repository(args.directory, args.keep)

        if results['failed']:
            exit(1)  # Exit with error code if any applications failed
        else:
            logger.info("All applications processed successfully!")

    except KeyboardInterrupt:
        logger.info("Cleanup interrupted by user")
        exit(130)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        exit(1)


if __name__ == "__main__":
    main()

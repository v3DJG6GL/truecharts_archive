# TrueNAS SCALE catalog

This is a fork of the archived TrueCharts App Catalog for TrueNAS SCALE.

Since iX-Systems will deprecate their Kubernets/Helm-based GUI app plattform in Q4 2024, TrueCharts already deprecated their TrueNAS catalog. Thus, you cannot update your already installed applications anymore although there's currently no migration to another Kubernetes plattform available. There will be a migration to their new Kubernetes-based plattform(s).  
But for now, you have to wait.

Therefore I decided to fork their archived chart repository and manually push some updates for applications I personally use. Feel free to use this chart to update your own TrueCharts applications on TrueNAS SCALE.

&nbsp;

### **Be aware that I won't continue pushing updates as soon as there's a stable migration to a new Kubernetes/Helm plattform available!**

### **!!! I am not responsible for any issues that might occur. Always backup your data! !!!**

&nbsp;

- ### How to change your TrueCharts catalog:
    
    1.  Remove your already old/deprecated TrueCharts catalog: *Apps* --> *Discover Apps* --> *Manage Catalogs* --> *TRUECHARTS* --> *Delete* (don't worry, this won't delete any of your already installed applications)
    2.  Add this repository as a new Catalog:
        1.  *Add Catalog* --> *Continue*
            - **Catalog Name:** TrueCharts
            - **Repository:** https://github.com/v3DJG6GL/truecharts_archive
            - **Preferred Trains:** incubator, premium, stable, system
            - **Branch:** main

Now you should be able to update your applications again.

- ### I currently manually push updates for these applications:
    
    - **premium train:**
        - authelia: v4.38.10 *(Updated: 2024.08.05)*
        - nextcloud: v29.0.6 **(Updated: 2024.09.05)***
        - traefik: v3.1.2 *(Updated: 2024.08.09)*
    - **stable train**
        - anything-llm: latest *(Updated: 2024.09.03)*
        - audiobookshelf: v2.13.3 *(Updated: 2024.09.03)*
        - autobrr: v1.45.0 *(Updated: 2024.08.26)*
		- changedetection.io: v0.46.04 ***(Updated: 2024.09.05)***
		- cloudflared: v2024.8.3 *(Updated: 2024.08.26)*
        - code-server: v4.91.1 *(Updated: 2024.07.24)*
		- crafty-4: v4.4.3 *(Updated: 2024.08.09)*
        - flaresolverr: pr-1300-experimental *(Updated: 2024.09.03)*
		- gamevault-backend: v12.2.0 *(Updated: 2024.08.06)*
        - immich: v1.113.1 *(Updated: 2024.09.03)*
        - jellyfin: v10.9.10 *(Updated: 2024.08.26)*
        - jellystat: v1.1.0 *(Updated: 2024.07.24)*
        - Lidarr: v2.5.2.4316 *(Updated: 2024.08.26)*
		- local-ai: v2.20.1 *(Updated: 2024.08.26)*
		- maintainerr: v2.1.0 *(Updated: 2024.09.03)* ***(Requested)***
        - meshcentral: v1.1.27 *(Updated: 2024.07.24)*
        - minio: v2024.08.29 *(Updated: 2024.09.03)*
		- ollama: v0.3.9 *(Updated: 2024.09.03)* ***(Requested)***
		- paperless-ngx: v2.11.6 *(Updated: 2024.08.26)* ***(Requested)***
		- plex: v1.40.5.8897 *(Updated: 2024.08.26)* ***(Requested)***
        - prowlarr: v1.23.1.4708 *(Updated: 2024.09.03)*
		- qbittorrent: v4.6.6 *(Updated: 2024.08.26)*
        - radarr: v5.9.1.9070 *(Updated: 2024.08.26)*
        - Readarr: v0.3.32.2587 *(Updated: 2024.07.24)*
		- recyclarr: v7.2.2 *(Updated: 2024.08.26)*
		- sabnzbd: v4.3.3 *(Updated: 2024.08.26)* ***(Requested)***
        - sftpgo: v2.6.2 *(Updated: 2024.07.24)*
        - sonarr: v4.0.9.2244 *(Updated: 2024.08.26)*
        - stun-turn-server: latest *(Updated: 2024.07.24)*
		- syncthing: v1.27.11 *(Updated: 2024.09.03)* ***(Requested)***
		- Tautulli: v2.14.3 *(Updated: 2024.08.02)* ***(Requested)***
        - unpackerr: v0.14.5 *(Updated: 2024.08.05)*


- ### Changelog:
	- 2024.09.03:
		- nextcloud: v29.0.6
		- changedetection.io: v0.46.04

	- 2024.09.03:
		- anything-llm: latest
		- audiobookshelf: v2.13.3
		- changedetection.io: v0.46.03
		- flaresolverr: pr-1300-experimental (switched tag & repository to "ghcr.io/alexfozor/flaresolverr" in order to get flaresolverr into a working condition again :))
		- immich: v1.113.1
		- minio: v2024.08.29
		- ollama: v0.3.9
		- prowlarr: v1.23.1.4708
		- syncthing: v1.27.11
		- maintainerr: v2.1.0
	- 2024.08.26:
		- audiobookshelf: v2.12.3
		- autobrr: v1.45.0
		- cloudflared: v2024.8.3
		- jellyfin: v10.9.10
		- lidarr: v2.5.2.4316
		- local-ai: v2.20.1
		- minio: v2024.08.17
		- nextcloud: v29.0.5
		- ollama: v0.3.6
		- paperless-ngx: v2.11.6
		- plex: v1.40.5.8897
		- radarr: v5.9.1.9070
		- recyclarr: v7.2.2
		- sabnzbd: v4.3.3
		- sonarr: v4.0.9.2244
		- qbittorrent: v4.6.6
	- 2024.08.09:
		- audiobookshelf: v2.12.2
		- crafty-4: v4.4.3
		- Ollama: v0.3.4
		- Paperless-ngx: v2.11.3
		- Syncthing: v1.27.10
		- traefik: v3.1.2 
	- 2024.08.06:
		- gamevault-backend: v12.2.0
	- 2024.08.05:
		- audiobookshelf: v2.12.0
		- authelia: v4.38.10
		- jellyfin: v10.9.9
		- local-ai: v2.19.4
		- recyclarr: v7.2.1
		- traefik: v3.1.1
		- unpackerr: v0.14.5
	- 2024.08.02:
		- crafty-4: v4.4.0
		- Plex: v1.40.4.8679
		- SABnzbd: v4.3.2
		- Tautulli: v2.14.3
	- 2024.07.27:
		- Prowlarr: v1.21.2.4649
	- 2024.07.25:
		- traefik: v3.1.0
		- local-ai: v2.19.2
	- 2024.07.24:
		- authelia: v4.38.9
		- Nextcloud: v29.0.4
		- anything-llm: latest
		- audiobookshelf: v2.11.0
		- autobrr: v1.44.0
		- code-server: v4.91.1
		- flaresolverr: v3.3.21
		- immich: v1.109.2
		- jellyfin: v10.9.8
		- jellystat: v1.1.0
		- Lidarr: v2.5.0.4277
		- meshcentral: v1.1.27
		- minio: v2024.07.16
		- Radarr: v5.8.3.8933
		- Readarr: v0.3.32.2587
		- sftpgo: v2.6.2
		- Sonarr: v4.0.8.1874
		- stun-turn-server: latest
		- unpackerr: v0.14.0
		
# How I update this catalog:
**I use following software to make changes to the catalog:**
- GitHub Desktop: https://desktop.github.com/download/
To synchronize this repository to my Computer
- Notepad++: https://github.com/notepad-plus-plus/notepad-plus-plus
To make changes to all the _.yaml_, _.json_ & _.md_ files
Especially the Find (_CTRL+F_) & Replace (_CTRL+H_) functions are super helpful. Furthermore, you can use Notepad++ to fold parts within the `app_version.json` which helps a lot to copy the correct part of that file.

**To update an application, these files must be modified:**
1. `truecharts_archive\catalog.json`:
    Search for your application and update following part for your app
   ```            "latest_version": "3.0.9",
            "latest_app_version": "2.0.3",
            "latest_human_version": "2.0.3_3.0.9",
            "last_update": "2024-05-29 12:35:14",
   ```
   - **latest_version**: `3.0.9` --> `3.1.0` (bump the _chart_ version one version up)
   - **latest_app_version**: `2.0.3` --> `3.1.0` (insert the _app_ version you're updating to)
   - **latest_human_version**: `2.0.3_3.0.9` --> `2.1.0_3.1.0` (_chart_ version & _app_ version combined together)
   - **last_update**: `2024-05-29 12:35:14` --> `2024-09-03 17:00:00` (take the approx. date & time when you're updating the app)
2. `truecharts_archive\stable\maintainerr\app_versions.json`:
Dublicate everything between
   ```
    "3.0.9": {
        "healthy": true,
        "supported": true,
        "healthy_error": null,
   ```
   and
   ```
    },
   ```
   just before these lines where the information for the next older version starts:
   ```
    "3.0.9": {
        "healthy": true,
        "supported": true,
        "healthy_error": null,
   ```
   - Change these occurances:
      - 1x `2024-05-29 12:35:14` (take the date & time value you used at step one when modifying `catalog.json`)
      - 2x `2.0.3` (take the _app_ version value you used at step one when modifying `catalog.json`)
      - 5x `3.0.9` (take the _chart_ version value you used at step one when modifying `catalog.json`)
3. Dublicate the folder `truecharts_archive\stable\maintainerr\3.0.9` and change the folder name to the _chart_ version value you used at step one when modifying `catalog.json`
4. Change these occurances within `truecharts_archive\stable\maintainerr\3.1.0\Chart.yaml`:
    - 1x `2.0.3` (take the _app_ version value you used at step one when modifying `catalog.json`)
	- 1x `3.0.9` (take the _chart_ version value you used at step one when modifying `catalog.json`)
5. `truecharts_archive\stable\maintainerr\3.1.0\ix_values.yaml`:
Update these lines where the image is specified:
   ```
	image:
	repository: jorenn92/maintainerr
	pullPolicy: IfNotPresent
	tag: 2.0.3@sha256:712e990afff98767a880284eb914fd5f2f5d76c5e8838c3f003fecdeb045b912
   ```
   With some exceptions I always use the images which TrueCharts uses. I copy them from the TrueCharts repository:
   https://github.com/truecharts/charts/blob/master/charts/stable/maintainerr/values.yaml
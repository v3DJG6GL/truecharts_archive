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
  1.  Remove your already old/deprecated TrueCharts catalog: _Apps_ --> _Discover Apps_ --> _Manage Catalogs_ --> _TRUECHARTS_ --> _Delete_ (don't worry, this won't delete any of your already installed applications)
  2.  Add this repository as a new Catalog:
      1.  _Add Catalog_ --> _Continue_
          - **Catalog Name:** TrueCharts
          - **Repository:** https://github.com/v3DJG6GL/truecharts_archive
          - **Preferred Trains:** incubator, premium, stable, system
          - **Branch:** main

Now you should be able to update your applications again.

- ### I currently manually push updates for these applications:

  - **premium train:**

    - authelia: v4.38.17 *(Updated: 2024.11.04)*
    - grafana: v11.2.0 *(Updated: 2024.09.18)* ***(Requested)***
    - nextcloud: v30.0.1 *(Updated: 2024.10.29)*
    - prometheus: v2.54.1 *(Updated: 2024.09.18)* ***(Requested)***
    - traefik: v3.2.0 *(Updated: 2024.10.29)*

  - **stable train**
    - anything-llm: latest *(Updated: 2024.09.03)*
    - audiobookshelf: v2.16.2 *(Updated: 2024.11.04)*
    - autobrr: v1.50.0 ***(Updated: 2024.11.14)***
    - bazarr: v1.4.5 *(Updated: 2024.10.03)*
    - changedetection.io: v0.47.06 ***(Updated: 2024.11.14)***
    - cloudflared: v2024.10.1 *(Updated: 2024.10.29)*
    - code-server: v4.93.1 *(Updated: 2024.10.03)*
    - codeproject-ai-server: v2.6.5 *(Updated: 2024.10.03)*
    - crafty-4: v4.4.4 *(Updated: 2024.10.03)*
    - factorio: stable *(Updated: 2024.09.18)*
	- frigate: v0.14.1 *(Updated: 2024.10.29)* ***(PR #29)***
    - flaresolverr: pr-1300-experimental *(Updated: 2024.09.03)*
    - gamevault-backend: v12.2.0 *(Updated: 2024.08.06)*
    - home-assistant: v2024.10.3 *(Updated: 2024.10.29)* ***(PR #29)***
    - immich: v1.120.2 ***(Updated: 2024.11.14)***
    - jellyfin: v10.10.1 *(Updated: 2024.11.04)*
    - jellystat: v1.1.0 *(Updated: 2024.07.24)*
    - lidarr: v2.7.1.4417 *(Updated: 2024.10.29)*
	- lldap: v0.6.0 ***(Updated: 2024.11.14)***
    - local-ai: v2.23.0 ***(Updated: 2024.11.14)***
    - maintainerr: v2.2.1 ***(Updated: 2024.11.14)*** ***(Requested)***
    - meshcentral: v1.1.33 *(Updated: 2024.11.04)*
    - minio: v2024.10.29 *(Updated: 2024.11.04)*
    - nzbget: v24.3 *(Updated: 2024.09.17)* ***(Requested)***
    - ollama: v0.4.1 ***(Updated: 2024.11.14)*** ***(Requested)***
    - paperless-ngx: v2.13.5 ***(Updated: 2024.11.14)*** ***(Requested)***
    - plex: v1.41.1.9057 *(Updated: 2024.10.29)* ***(Requested)***
    - prowlarr: v1.26.0.4833 *(Updated: 2024.11.04)*
    - qbitmanage: v4.1.9 *(Updated: 2024.09.18)* ***(Requested)***
    - qbittorrent: v5.0.1 *(Updated: 2024.10.29)*
    - radarr: v5.14.0.9383 *(Updated: 2024.10.29)*
    - readarr: v0.4.3.2665 *(Updated: 2024.11.04)*
    - recyclarr: v7.4.0 ***(Updated: 2024.11.14)***
    - satisfactory: v1.8.6 *(Updated: 2024.09.24)* ***(Requested)***
    - sabnzbd: v4.3.3 *(Updated: 2024.08.26)* ***(Requested)***
    - sftpgo: v2.6.2 *(Updated: 2024.07.24)*
    - sonarr: v4.0.10.2544 *(Updated: 2024.10.29)*
    - stun-turn-server: latest *(Updated: 2024.09.18)*
    - syncthing: v1.27.12 *(Updated: 2024.09.16)* ***(Requested)***
    - tautulli: v2.14.6 *(Updated: 2024.10.13)* ***(Requested)***
    - unpackerr: v0.14.5 *(Updated: 2024.08.05)*

- ### Changelog:

  - 2024.11.14:
	- autobrr: v1.50.0
	- changedetection.io: v0.47.06
	- immich: v1.120.2
	- lldap: v0.6.0
	- local-ai: v2.23.0
	- maintainerr: v2.2.1
	- ollama: v0.4.1
	- paperless-ngx: v2.13.5
	- recyclarr: v7.4.0

  - 2024.11.04:
	- audiobookshelf: v2.16.2
	- authelia: v4.38.17
	- changedetection.io: v0.47.05
	- jellyfin: v10.10.1
	- meshcentral: v1.1.33
	- minio: v2024.10.29
	- paperless-ngx: v2.13.4
	- prowlarr: v1.26.0.4833
	- readarr: v0.4.3.2665

  - 2024.10.29:
	- audiobookshelf: v2.16.1
	- autobrr: v1.48.0
	- changedetection.io: v0.47.04
	- cloudflared: v2024.10.1
	- frigate: v0.14.1 (PR #29)
	- home-assistant: v2024.10.3 (PR #29)
	- immich: v1.119.0
	- jellyfin: v10.10.0
	- lidarr: v2.7.1.4417
	- local-ai: v2.22.1
	- nextcloud: v30.0.1
	- ollama: v0.3.14
	- paperless-ngx: v2.13.1
	- plex: v1.41.1.9057
	- prowlarr: v1.25.4.4818
	- qbittorrent: v5.0.1
	- radarr: v5.14.0.9383
	- readarr: v0.4.2.2653
	- recyclarr: v7.3.0
	- sonarr: v4.0.10.2544
	- traefik: v3.2.0 

  - 2024.10.17:
	- immich: v1.118.2
    - minio: v2024.10.13
	- syncthing: v1.28.0

  - 2024.10.13:
    - audiobookshelf: v2.15.0
    - changedetection.io: v0.47.03
    - local-ai: v2.22.0
    - ollama: v0.3.13
    - prowlarr: v1.25.2.4794
    - radarr: v5.12.2.9335
    - tautulli: v2.14.6

  - 2024.10.10:
    - lidarr: v2.6.4.4402

  - 2024.10.08:
    - audiobookshelf: v2.14.0
    - authelia: v4.38.16
    - autobrr: v1.47.1
    - prowlarr: v1.25.1.4770

  - 2024.10.06:
    - lidarr: v2.5.3.4341
    - prowlarr: v1.25.0.4759
    - readarr: v0.4.0.2634

  - 2024.10.03
    - authelia: v4.38.15
    - bazarr: v1.4.5
    - code-server: v4.93.1
    - codeproject-ai-server: v2.6.5
    - crafty-4: v4.4.4
    - immich: v1.117.0
    - local-ai: v2.21.1
    - meshcentral: v1.1.32
    - minio: v2024.10.02
    - plex: v1.41.0.8994
    - prowlarr: v1.24.3.4754
    - qbittorrent: v5.0.0
    - traefik: v3.1.5

  - 2024.09.25:
    - minio: v2024.09.22
    - ollama: v0.3.12
    - radarr: v5.11.0.9244

  - 2024.09.24:
    - authelia: v4.38.12
    - prowlarr: v1.24.1.4740 (PR #20)
    - radarr: v5.10.4.9218
    - satisfactory: v1.8.6 (PR #22)
    - tautulli: v2.14.5 (PR #21)

  - 2024.09.20:
    - nextcloud: v30.0.0
    - ollama: v0.3.11
    - traefik: v3.1.4 (fixes CVE-2024-45410)

  - 2024.09.18:
    - factorio: stable (PR #17)
    - grafana: v11.2.0 (PR #17)
    - prometheus: v2.54.1 (PR #17)
    - qbitmanage: v4.1.9 (PR #17)
    - qbittorrent: v4.6.7
    - stun-turn-server: latest
    - traefik: v3.1.3

  - 2024.09.17:
    - nzbget: v24.3 (PR #13)

  - 2024.09.16:
    - audiobookshelf: v2.13.4
    - autobrr: v1.46.1
    - bazarr: v1.4.4
    - immich: v1.115.0
    - jellyfin: v10.9.11
    - maintainerr: v2.1.2
    - meshcentral: v1.1.30
    - minio: v2024.09.13
    - ollama: v0.3.10
    - paperless-ngx: v2.12.1
    - plex: v1.41.0.8992
    - prowlarr: v1.24.0.4721
    - recyclarr: v7.2.4
    - syncthing: v1.27.12

  - 2024.09.05:
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
   ```"latest_version": "3.0.9",
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

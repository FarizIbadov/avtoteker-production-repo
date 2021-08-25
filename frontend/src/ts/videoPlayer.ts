import axios from "axios";

class VideoPlayer {
  loaded = false;
  videoContainer: HTMLDivElement;
  isFullscreen: boolean = false;
  video?: HTMLVideoElement;
  source?: HTMLSourceElement;
  fullscreenBtn?: HTMLButtonElement;
  range?: HTMLInputElement;
  playPauseBtn?: HTMLButtonElement;
  duration?: number;
  videoToolContainer?: HTMLElement;
  loadingSpinner = `
      <div class="text-center text-light video-spinner" id="video-spinner">
        <div class="spinner-border" style="width: 5rem; height: 5rem;" role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </div>
    `;

  constructor(id: string) {
    this.videoContainer = document.querySelector(`.${id}`) as HTMLDivElement;

    if (this.videoContainer) {
      this.video = this.videoContainer.querySelector(
        "video",
      ) as HTMLVideoElement;

      this.videoToolContainer = this.videoContainer.querySelector(
        ".video-tool-container",
      ) as HTMLElement;

      if (this.video) {
        this.source = this.video.querySelector("source") as HTMLSourceElement;
        this.configureBlobUrl();
        this.configFullscreen();
        this.configVideo();
        this.configPlayPause();
      }
    }
  }
  configPlayPause() {
    this.playPauseBtn = this.videoContainer.querySelector(
      ".video-play-pause",
    ) as HTMLButtonElement;

    if (this.playPauseBtn) {
      this.playPauseBtn.addEventListener("click", () => {
        this.setPlayPause();
      });
    }

    document.addEventListener("keyup", e => {
      e.preventDefault();
      switch (e.code) {
        case "Space":
          this.setPlayPause();
          return;
        case "KeyF":
          this.setFullscreen();
          return;
        default:
          return;
      }
    });
  }

  setPlayPause = () => {
    if (this.video!.paused) {
      this.setPlay();
    } else {
      this.setPause();
    }
  };

  setPlay = () => {
    const promise = this.video!.play();
    if (promise != undefined) {
      promise.then(() => {
        this.playPauseBtn!.innerHTML =
          '<i class="bi bi-pause-fill d-flex align-items-center h-100"></i>';
      });
    }
  };

  setPause = () => {
    this.video!.pause();
    this.playPauseBtn!.innerHTML =
      '<i class="bi bi-play-fill d-flex align-items-center h-100"></i>';
  };

  configVideo() {
    if (this.video) {
      this.video.addEventListener("timeupdate", e => {
        e.preventDefault();
        const { duration, currentTime } = this.video!;
        this.duration = duration;
        const value = (currentTime / duration) * 100;
        if (value <= 100) {
          this.range!.value = String(value);
          this.setInputBackground(value);
        }
      });

      this.video.addEventListener("loadedmetadata", e => {
        e.preventDefault();
        this.setPlayPause();
        this.configRange();

        const spinner = document.getElementById("video-spinner");
        if (spinner) {
          spinner.remove();
        }

        if (this.videoToolContainer) {
          this.videoToolContainer.classList.remove("d-none");
          this.videoToolContainer.classList.add("d-flex");
        }

        if (!this.loaded) {
          var x = window.matchMedia("(min-width: 768px)");
          if (x.matches) {
            this.video!.addEventListener("click", () => {
              this.setPlayPause();
            });
          }
          this.loaded = true;
        }
      });

      this.video.addEventListener("ended", () => {
        this.video!.currentTime = 0;
        this.video!.play();
      });
    }
  }

  configRange = () => {
    this.range = this.videoContainer.querySelector(
      ".video-progress",
    ) as HTMLInputElement;

    if (this.range) {
      const value = this.range.value;
      this.setInputBackground(value);
      this.range.addEventListener("input", this.rangeHandler);
    }
  };

  rangeHandler = (e: Event) => {
    const { value } = e.target as HTMLInputElement;
    this.setInputBackground(value);
    const currentTime = (+value / 100) * this.duration!;
    if (isFinite(currentTime)) {
      this.video!.load();
      this.video!.currentTime = currentTime;
    }
  };

  setInputBackground = (value: string | number) => {
    this.range!.style.background = `linear-gradient(to right, #fb0 0% ${value}%, #fff ${value}% 100%)`;
  };

  configureBlobUrl = () => {
    const src = this.source!.getAttribute("src") as string;
    this.videoContainer.insertAdjacentHTML("afterbegin", this.loadingSpinner);
    axios
      .get(src, { responseType: "blob" })
      .then(res => this.setObjectUrl(res.data))
      .catch(err => {
        console.log(err);
      });
  };

  setObjectUrl = (object: any) => {
    const url = URL.createObjectURL(object);
    this.source!.setAttribute("src", url);
  };

  configFullscreen = () => {
    this.fullscreenBtn = this.videoContainer.querySelector(
      ".fullscreen-btn",
    ) as HTMLButtonElement;
    if (this.fullscreenBtn) {
      this.fullscreenBtn.addEventListener("click", this.setFullscreen);
    }

    document.addEventListener("fullscreenchange", e => {
      if (document.fullscreenElement) {
        this.isFullscreen = true;
        this.fullscreenBtn!.innerHTML = "<i class='bi bi-fullscreen-exit'></i>";
      } else {
        this.isFullscreen = false;
        this.fullscreenBtn!.innerHTML = "<i class='bi bi-fullscreen'></i>";
      }
    });
  };

  setFullscreen = () => {
    if (!this.isFullscreen) {
      this.videoContainer.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  };
}

new VideoPlayer("video-player");

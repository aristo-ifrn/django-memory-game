const HTMLElements = {
  loadingWrapper: document.querySelector("#loading"),
  homeButton: document.querySelector("#home"),
  selectableButtons: Array.from(document.querySelectorAll(".selectable")),
  clickableButtons: Array.from(document.querySelectorAll(".clickable")),
  loadingPopUp: document.querySelector("#loading"),
};

const tracks = {
  focus: new Audio("/static/assets/audios/focus.wav"),
  select: new Audio("/static/assets/audios/select.wav"),
};

const setVolumeForAudios = (volume) => {
  Object.values(tracks).forEach((track) => (track.volume = volume));
};

const loadVolumeFromLocalStorage = () => {
  const savedVolume = parseFloat(localStorage.getItem("volume")) || 1.0;
  setVolumeForAudios(savedVolume);
};

HTMLElements.selectableButtons.forEach((element) => {
  element.addEventListener("mouseenter", () => {
    tracks.focus.play();
  });
});

HTMLElements.clickableButtons.forEach((element) => {
  element.addEventListener("click", () => {
    tracks.select.play();
  });
});

const redirectWithLoading = (url, delay = 1000) => {
  HTMLElements.loadingPopUp.setAttribute("data-state", "opened");
  setTimeout(() => (location.href = url), delay);
};

function getRootUrl() {
  return window.location.origin
    ? window.location.origin + "/"
    : window.location.protocol + "/" + window.location.host + "/";
}

HTMLElements.homeButton.addEventListener("click", () => {
  redirectWithLoading(getRootUrl(), 1000);
});

window.addEventListener("load", () => {
  HTMLElements.loadingWrapper.setAttribute("data-state", "closed");
  loadVolumeFromLocalStorage();
});

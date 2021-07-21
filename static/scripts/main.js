
const speechTranscriptContainer = document.querySelector(".speechTranscriptContainer > p")

function animateLoader() {
    speechTranscriptContainer.classList.add("loader")
}

function onPLoad() {
    speechTranscriptContainer.classList.remove("loader")
}


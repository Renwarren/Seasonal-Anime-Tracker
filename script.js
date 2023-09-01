var iframe = document.querySelector('.video-iframe');

function playVideo() {
iframe.src = iframe.src.replace('autoplay=0', 'autoplay=1');
}

function pauseVideo() {
iframe.src = iframe.src.replace('autoplay=1', 'autoplay=0');
}
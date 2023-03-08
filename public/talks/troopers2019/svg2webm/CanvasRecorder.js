"use strict";


class CanvasRecorder {
	constructor(options) {
		const canvas = options.canvas,
			callback = options.callback;

		let framerate = 0;

		const stream = canvas.captureStream(framerate),
			track = stream.getVideoTracks && stream.getVideoTracks()[0];

		const chunks = [];
		const recorder = new MediaRecorder(stream, { mimeType: "video/webm", videoBitsPerSecond: 3000000 });

		recorder.ondataavailable = function(e) {
			const blob = e.data;
			if (blob && blob.size) { chunks.push(blob); }
		};

		recorder.onstop = (e) => {
			//console.log('stop', e);
			const blob = new Blob(chunks, { type: "video/webm" });
			callback(blob);
		};

		this.recorder = recorder;
		this.track = track;
	}

	start() {
		this.recorder.start();
	}

	stop() {
		this.recorder.stop();
	}

	requestFrame() {
		this.track.requestFrame();
	}
}


function renderSvg(svgDocument, canv, frameCallback) {
	const EventEmitter = require('events');
	const ev = new EventEmitter();

	const svg = svgDocument.getRootNode();
	const ctx = canv.getContext('2d');
	const screen = svgDocument.getElementById("screen");
	const terminal = svgDocument.getElementById("terminal");
	console.log(svg);

	const viewBox = terminal.getAttribute("viewBox").split(" ").map(parseFloat);
	let svgWidth  = viewBox[2];
	let svgHeight  = viewBox[3];
	canv.width  = svgWidth * 2;
	canv.height  = svgHeight * 2;
	console.log("The size is", canv.width, canv.height);

	const duration = parseInt(svgDocument
		.getElementsByTagName("style")[0]
		.innerHTML
		.match(/--animation-duration: (\d+)ms;/)[1]);
	console.log("The duration is", duration);

	const recorder = new CanvasRecorder({
		canvas: canv,
		callback: blob => {
			ev.emit('finish', blob);
		},
	});

	const animes = Array.from(svgDocument.getElementsByTagName("animate"));
	const aniBegins = animes.map(x => 
		({
			animate: x,
			begin: parseInt(x.getAttribute("begin")),
			dur: parseInt(x.getAttribute("dur"))
		})
	);

	function freeze(time) {
		screen.pauseAnimations();
		aniBegins.forEach(x=> {
			x.animate.setAttribute("begin", (x.begin - time) + "ms");
		});
		screen.setCurrentTime(0);
	}

	function svg2canvas(callback) {
		const serialized = new XMLSerializer().serializeToString(svg);
		const url = URL.createObjectURL(new Blob([serialized], { type: "image/svg+xml" }));
	
		const img = new Image();
		img.onload = function() {
			ctx.drawImage(img, 0, 0, svgWidth, svgHeight, 0, 0, canv.width, canv.height);
			callback();
		};
		img.src = url;
	}

	function render(time, frame, callback) {
		ev.emit('progress', time / duration);
		freeze(time);
		svg2canvas(callback);
	}

	function renderLoop(frameNum) {
		let animTime = frameNum * 100;
		if (animTime > duration) {
			ev.emit('finish', null);
			return;
		}

		let next = () => renderLoop(frameNum + 1);
		render(animTime, frameNum, () => {
			if (frameCallback) {
				frameCallback(frameNum, next);
			} else {
				next();
			}
		});
	}
	
	renderLoop(0);

	return ev;
}

module.exports = renderSvg;



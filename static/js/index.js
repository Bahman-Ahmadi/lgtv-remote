function send(code) {
	return new Promise ((res)=> {
		let xhr = new XMLHttpRequest();
		xhr.onload = async function (e) {
			if (this.readyState == 4 && this.status == 200) {
				var response = JSON.parse(this.responseText);
				console.log(this.responseText);

				document.getElementById("channel").innerHTML = response.channel;
				document.getElementById("volume").innerHTML = response.volume;
				document.getElementById("mute").innerHTML = response.isMute ? '<i class="bi bi-volume-mute-fill" id="muteIc"></i>': '<i class="bi bi-volume-up-fill" id="muteIc"></i>';
			}
			return;
		};
		xhr.onerror = function (e) {
			console.log(e);
		};
		xhr.open("POST", "http://127.0.0.1:5000/handler?code="+code, true);
		xhr.send();
	});
}

function Type(text) {
	var input = document.getElementById("channelInput");
	if (input.innerHTML.length < 2) {
		input.innerHTML += text;
	}
}
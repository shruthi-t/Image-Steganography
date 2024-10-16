// Encrypt text into the image
function encryptText() {
    const imageInput = document.getElementById("encryptImageInput").files[0];
    const text = document.getElementById("encryptText").value;
    const canvas = document.getElementById("encryptCanvas");
    const ctx = canvas.getContext("2d");

    if (!imageInput || !text) {
        alert("Please select an image and enter some text.");
        return;
    }

    const reader = new FileReader();
    reader.onload = function (event) {
        const img = new Image();
        img.onload = function () {
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);

            // Embed text into the image pixel data
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const pixels = imageData.data;

            for (let i = 0; i < text.length; i++) {
                pixels[i * 4] = text.charCodeAt(i); // Store the text in the red channel
            }

            ctx.putImageData(imageData, 0, 0);
            const encryptedImageURL = canvas.toDataURL("image/png");
            downloadImage(encryptedImageURL, "encrypted-image.png");
        };
        img.src = event.target.result;
    };
    reader.readAsDataURL(imageInput);
}

// Download encrypted image
function downloadImage(url, filename) {
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
}

// Decrypt text from the image
function decryptText() {
    const imageInput = document.getElementById("decryptImageInput").files[0];
    const textLength = parseInt(document.getElementById("decryptTextLength").value);
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");

    if (!imageInput || isNaN(textLength)) {
        alert("Please select an image and enter the length of the text.");
        return;
    }

    const reader = new FileReader();
    reader.onload = function (event) {
        const img = new Image();
        img.onload = function () {
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);

            // Extract text from the image pixel data
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const pixels = imageData.data;
            let decryptedText = "";

            for (let i = 0; i < textLength; i++) {
                decryptedText += String.fromCharCode(pixels[i * 4]); // Extract text from red channel
            }

            // Display the decrypted text in the textarea
            document.getElementById("decryptedTextBox").value = decryptedText;
        };
        img.src = event.target.result;
    };
    reader.readAsDataURL(imageInput);
}

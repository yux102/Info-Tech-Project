function loadPage() {
    let totalWidth = document.getElementById("submitForm").offsetWidth;
    let buttonWidth = document.getElementById("submitFormButton").offsetWidth;
    document.getElementById("submitFormInput").style.width =
        (totalWidth - buttonWidth - 20).toString() + "px";
}

function openPDF(pdfName) {
    document.getElementById("pdfDisplay").remove();
    $('#pdf').append($('<iframe id="pdfDisplay" src="" width="100%" height="100%">'));

    document.getElementById("pdfDisplay").src = pdfName;
}

function openWeb(url) {

    document.getElementById("pdfDisplay").src = url;
}
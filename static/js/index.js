const botInviteUrl = "https://discordapp.com/oauth2/authorize?&client_id=494573728454279178&scope=bot&permissions=8";
const supportInviteUrl = "https://discord.gg/VjsUafD";
const windowArgs = "top=50, left=325, width=350, height=600, status=no, scrollbars=yes";
const http = new XMLHttpRequest();

function inviteLink() {
    open(botInviteUrl, '', windowArgs);
    return false;
}

function supportLink() {
    open(supportInviteUrl, '', windowArgs);
    return false;
}

function setLang(url, new_lang) {
    http.open("GET", url + "?new_lang=" + new_lang, true);
    http.send();
}

http.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        location.reload();
    }
}

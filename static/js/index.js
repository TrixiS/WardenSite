const botInviteUrl = "https://discordapp.com/oauth2/authorize?&client_id=494573728454279178&scope=bot&permissions=8";
const supportInviteUrl = "https://discord.gg/VjsUafD";
const windowArgs = "top=50, left=325, width=350, height=600, status=no, scrollbars=yes";

function inviteLink() {
    open(botInviteUrl, '', windowArgs);
    return false;
}

function supportLink() {
    open(supportInviteUrl, '', windowArgs);
    return false;
}

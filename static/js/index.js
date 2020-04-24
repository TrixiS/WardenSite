const botInviteUrl = "https://discordapp.com/oauth2/authorize?&client_id=494573728454279178&scope=bot&permissions=8";
const supportInviteUrl = "https://discord.gg/VjsUafD";

function inviteLink() {
    open(botInviteUrl, '', 'top=50, left=325, width=350, height=600, status=no, scrollbars=yes');
    return false;
}

function supportLink() {
    open(supportInviteUrl, '', 'top=50, left=325, width=350, height=600, status=no, scrollbars=yes');
    return false;
}

# CSNETWK-MP

Additional Features implemented:

## Requiered Libraries
socket
ast

## Channel feature
```
/createc <channel_name>              create a channel in the server. User becomes channel owner and admin.

/invitec <channel_name> <handle>     invite a user to the channel. Can only be done by channel admins.
/acceptc <channel_name>              accept an invitation to a channel. Can only be done if user is invited.
/declinec <channel_name>             notifies all members of <channel_name> that user has declined their invitation. Can only be done if user is invited.

/promote <channel_name> <handle>     promote <handle> to the status of channel admin. Can only be done by channel admins. 
/demote <channel_name> <handle>      demote <handle> to the status of channel member. Can only be done by channel admins.
/kick <channel_name> <handle>        remove <handle> from a channel. Can only be done by channel admins.
/msgch <channel_name> <message>      messages all members of a channel with <message>

/leavec <channel_name>               leave a channel if and only if the user has joined
/deletec <channel_name>              delete a channel. Can only be done by channel owner.
```

## Block feature
```
/block <handle>                      ignores any incoming messages from <handle>. <handle> will be notified that they are blocked by the user.
/unblock <handle>                    unblocks <handle> if they were blocked by the user. 
```

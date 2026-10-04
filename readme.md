# Authorization Rules

| Action | OWNER | ADMIN | MEMBER |
|---|---|---|---|
| Create organization | Yes | — | — |
| Become organization owner | Creator | — | — |
| Invite organization members | Yes | Yes | No |
| Remove organization members | Yes | No | No |
| Remove owner | No | No | No |
| Create project | Yes | Yes | No |
| Delete project | Yes | No | No |
| Create task | Yes | Yes | **Yes\*** |
| Assign task | Yes | Yes | No |
| Modify another member's task | No | Yes | No |
| Access organization data | Yes | Yes | Yes, if member |
| Access project | Yes | Yes | **Only if project member** |
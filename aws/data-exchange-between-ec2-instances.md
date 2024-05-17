# TL;DR
Do not use public address. Use private address instead. Change inbound rule in advance.

# How to do it
1. Get private IPv4 address.
    1. Go to the `EC2 Dashboard`.
    2. In the `Resources` section, click `instances`.
    3. Select an instance among the list.
    4. Expand `details pane`.
    5. Find `Private IPv4 addresses` section.
2. Modify EC2 instance inbound rule.
    1. Go to thw `Security Group` setting.
    2. Click `Security group ID` to change.
        - It will lead to the details page of the security group.
    3. Click `Inbound rules` tab.
    4. Click `Edit inbound rules` button.
        - It will lead to the `Edit inbound rules` page.
    5. Click `Add rule` button located bottom left.
    6. Select `SSH` from a drop-down menu located in the `Type` column.
    7. Select `Custom` from a drop-down menu from the `Source` column.
    8. Click text box with :mag:, next to the `Source` column. It will show drop-down menu for presets.
    9. Assuming to allow inbound from a security group that another EC2 instance belongs to, click desired security group under the `Security Groups` section of the drop-down menu.
    10. Click `Save rules`.
3. Build `SCP` command.
    1. An EC2 instance that request data from the instance which we changed inbound setting above must have private key to access the instance.
    2. The example SCP command is:
        ```bash
        scp -i /private/key.pem -r ubuntu@pri.vate.ip4.address:/home/ubuntu/files_to_request /home/ubuntu/
        ```
# EC2 Instance Creation
- Check informations about instance types [here](https://aws.amazon.com/ec2/instance-types/)
- During the Amazon Machine Image (AMI) selection, be careful about `Supported EC2 instnaces` information.
- In the `Configure storage` section, set enough root volume size.
- You can access `instance store volumes`, so don't add new volume other than the root volume when it's not necessary.
- When setting inbound rules, make use of `CIDR` ([Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)).
    - For example, want to grant inbound access to ip address `123.346.789.*`, enter ip address like this: `123.346.789.0/24`.
    - This will reduce bothersome frequent inboud ip setting, especially when using a dynamic ip address, e.g. using VPN.

# User Names
Each AMI has different [default user names](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html#ami-default-user-names).

- For AL2023, Amazon Linux 2, or the Amazon Linux AMI, the user name is `ec2-user`.
- For an Ubuntu AMI, the user name is `ubuntu`.

> If you get error like this, but when every thing seems ok, review your user name:\
> EC2 ssh Permission denied (publickey,gssapi-keyex,gssapi-with-mic)\
> E.g. ssh -i private-key ec2-user@amazon.ec2.url

# Accessing Instance Store Volumes
Reference: [Make instance store volumes available on your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-instance-store-volumes.html#making-instance-stores-available-on-your-instances)
1. Check volumes that are formatted and mounted:
    ```bash
    $ df -h
    Filesystem                      Size  Used Avail Use% Mounted on
    /dev/root                       194G   48G  146G  25% /
    tmpfs                            91G     0   91G   0% /dev/shm
    tmpfs                            37G  1.4M   37G   1% /run
    tmpfs                           5.0M     0  5.0M   0% /run/lock
    /dev/nvme0n1p15                 105M  6.1M   99M   6% /boot/efi
    /dev/mapper/vg.01-lv_ephemeral  3.4T   28K  3.2T   1% /opt/dlami/nvme
    tmpfs                            19G  4.0K   19G   1% /run/user/1000
    ```

2. Check any volumes that were mapped at launch but not formatted and mounted.
    ```bash
    $ lsblk
    NAME                 MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
    loop0                  7:0    0  24.9M  1 loop /snap/amazon-ssm-agent/7628
    loop1                  7:1    0  55.7M  1 loop /snap/core18/2812
    loop2                  7:2    0  63.9M  1 loop /snap/core20/2182
    loop3                  7:3    0    87M  1 loop /snap/lxd/27037
    loop4                  7:4    0  40.4M  1 loop /snap/snapd/20671
    loop5                  7:5    0  38.7M  1 loop /snap/snapd/21465
    loop6                  7:6    0  55.7M  1 loop /snap/core18/2823
    loop7                  7:7    0    87M  1 loop /snap/lxd/28373
    nvme0n1              259:0    0   200G  0 disk 
    ├─nvme0n1p1          259:1    0 199.9G  0 part /
    ├─nvme0n1p14         259:2    0     4M  0 part 
    └─nvme0n1p15         259:3    0   106M  0 part /boot/efi
    nvme1n1              259:4    0 875.4G  0 disk 
    └─vg.01-lv_ephemeral 253:0    0   3.4T  0 lvm  /opt/dlami/nvme
    nvme2n1              259:5    0 875.4G  0 disk 
    └─vg.01-lv_ephemeral 253:0    0   3.4T  0 lvm  /opt/dlami/nvme
    nvme3n1              259:6    0 875.4G  0 disk 
    └─vg.01-lv_ephemeral 253:0    0   3.4T  0 lvm  /opt/dlami/nvme
    nvme4n1              259:7    0 875.4G  0 disk 
    └─vg.01-lv_ephemeral 253:0    0   3.4T  0 lvm  /opt/dlami/nvme
    ```

3. Create soft link.
    ```bash
    ln -s /opt/dlami/nvme ~/mydirectory
    ```
    > Don't forget to use `-s` to make it a soft link.
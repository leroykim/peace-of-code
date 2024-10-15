# Uploading files to Samba drive

## Mount Samba drive to local drive
1. Create `mnt` directory in a desired location. The file name does not matter.
    ```bash
    cd ~
    mkdir mnt
    ```
2. Mount Samba drive to the `mnt` directory.
    ```bash
    mount -t smbfs smb://<samba drive url>/<target directory path> ~/mnt
    ```

3. The `mnt` directory will be soft-linked to the `<target directory>`.

## Send files with `rsync`. 
> Use the directory name `mnt` instead of the `<target directory>` name!
```bash
rsync -avz ~/datasets/dataset_01 ~/mnt/<destination directory>
```
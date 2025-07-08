#!/usr/bin/env bash

# e - script stops on error (any internal or external return !=0)
# u - error if undefined variable
# o pipefail - script fails if one of piped command fails
# x - output each line (debug)
set -euo pipefail

SOURCE="/home/ec2-user/"
EFS_MOUNTPOINT="/mnt/efs-proticket"
EFS_DNS="fs-05b4d5bb440b07142.efs.us-east-1.amazonaws.com"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

mount_efs() {
    mkdir -p "${EFS_MOUNTPOINT}"

    if ! mountpoint -q "${EFS_MOUNTPOINT}"; then
        log "NO EFS mounted on the system"
        log "Mounting into '${EFS_MOUNTPOINT}'..."
        # Flags from AWS to attach the EFS through NFS
        mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport "${EFS_DNS}":/ "${EFS_MOUNTPOINT}"
        log "Done"
    fi
}

create_target_dir() {
    target="${EFS_MOUNTPOINT}/$(date +%Y-%m-%d)"
    mkdir -p "${target}"
    echo "${target}"
}

backup() {
    log "Target dir: '${1}'"
    rsync -avh "${SOURCE}" "${1}"
}

# -----------------------------------------------------------------------------

log "========================="
log "Starting backup script..."

mount_efs

backup_dir=$(create_target_dir)

backup "${backup_dir}"

log "Backup Done"
log "========================="

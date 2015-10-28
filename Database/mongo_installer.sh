 #!/bin/bash
COMPONENT="MongoDB Installer"
FILE="mongodb-osx-x86_64-3.0.7.tgz"
URL="https://fastdl.mongodb.org/osx/$FILE"

CURR="`pwd`"
# echo $CURR
DB="/data/db"
FULL_DB_PATH=$CURR$DB

function DL_MONGODB {
  wget $URL -P $CURR
}
function UNPACK {
  # Note that if your tarball already contains a directory name you want to change, add the --strip-components=1 option
  tar -zxvf $CURR/$FILE --directory mongodb --strip-components=1
}
function CR_DIRS {
  # Create /mongodb
  mkdir -p $CURR/mongodb
  # Create /data/db/
  mkdir -p $CURR$DB
  # Chmod the Database directory
  chmod +x $CURR/data/db
  # Create Log Directory
  mkdir -p $CURR/log
}
function EX_PATH {
  export PATH=$CURR/mongodb/bin:$PATH
}
function START {
  "$CURR/mongodb/bin/mongod --dbpath $FULL_DB_PATH --pidfilepath $CURR/mongodb.pid --logpath $CURR/log/mongodb.log --verbose" &
  # .$CURR/mongodb/bin/mongod
}

# Backup /data/db
# tar -cZf /var/my-backup.tgz /home/me/


# Download MongoDB
DL_MONGODB
# Create MongoDB Directory
CR_DIRS
# Unpack MongoDB
UNPACK
# Export mongod Path
EX_PATH
# Start MongoDB
START

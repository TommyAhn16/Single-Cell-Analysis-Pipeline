# Minimap2 installation
yum install -y install zlib-devel
wget https://github.com/lh3/minimap2/archive/v2.7.tar.gz
tar -xzvf v2.7.tar.gz
cd minimap2-2.7
make
cd ..
mv ./minimap2-2.7/minimap2 ./tools/.
rm -rf v2.7.tar.gz
rm -rf minimap2-2.7
# bedtools2 installation
wget https://github.com/arq5x/bedtools2/releases/download/v2.30.0/bedtools.static.binary
mv bedtools.static.binary tools/bedtools
chmod 777 tools/bedtools
# Freebayes installation
wget https://github.com/ekg/freebayes/releases/download/v1.3.1/freebayes-v1.3.1
mv freebayes-v1.3.1 ./tools/freebayes
chmod 777 ./tools/freebayes
# Vartrix installation
wget https://github.com/10XGenomics/vartrix/releases/download/v1.1.22/vartrix_linux
mv vartrix_linux ./tools/vartrix
chmod 777 ./tools/vartrix
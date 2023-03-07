CORENLP=stanford-corenlp-full-2015-12-09
SPICELIB=~/anaconda3/envs/blip/lib/python3.10/site-packages/pycocoevalcap/spice/lib
JAR=stanford-corenlp-3.6.0

DIR="$( cd "$(dirname "$0")" ; pwd -P )"
cd $DIR

echo "Downloading..."
wget http://nlp.stanford.edu/software/$CORENLP.zip
echo "Unzipping..."
unzip $CORENLP.zip -d $SPICELIB/
mv $SPICELIB/$CORENLP/$JAR.jar $SPICELIB/
mv $SPICELIB/$CORENLP/$JAR-models.jar $SPICELIB/
rm -f $CORENLP.zip
rm -rf $SPICELIB/$CORENLP/
echo "Done."

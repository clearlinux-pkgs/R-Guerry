#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-Guerry
Version  : 1.8.3
Release  : 47
URL      : https://cran.r-project.org/src/contrib/Guerry_1.8.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Guerry_1.8.3.tar.gz
Summary  : Maps, Data and Methods Related to Guerry (1833) "Moral
Group    : Development/Tools
License  : GPL-2.0
Requires: R-sp
BuildRequires : R-sp
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
graphic methods related to Guerry's "Moral Statistics of France". The goal is to facilitate the exploration and
	development of statistical and graphic methods for multivariate data in a geospatial context of historical interest.

%prep
%setup -q -n Guerry
pushd ..
cp -a Guerry buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698246114

%install
export SOURCE_DATE_EPOCH=1698246114
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Guerry/DESCRIPTION
/usr/lib64/R/library/Guerry/INDEX
/usr/lib64/R/library/Guerry/Meta/Rd.rds
/usr/lib64/R/library/Guerry/Meta/data.rds
/usr/lib64/R/library/Guerry/Meta/demo.rds
/usr/lib64/R/library/Guerry/Meta/features.rds
/usr/lib64/R/library/Guerry/Meta/hsearch.rds
/usr/lib64/R/library/Guerry/Meta/links.rds
/usr/lib64/R/library/Guerry/Meta/nsInfo.rds
/usr/lib64/R/library/Guerry/Meta/package.rds
/usr/lib64/R/library/Guerry/Meta/vignette.rds
/usr/lib64/R/library/Guerry/NAMESPACE
/usr/lib64/R/library/Guerry/NEWS.md
/usr/lib64/R/library/Guerry/WORDLIST
/usr/lib64/R/library/Guerry/data/Rdata.rdb
/usr/lib64/R/library/Guerry/data/Rdata.rds
/usr/lib64/R/library/Guerry/data/Rdata.rdx
/usr/lib64/R/library/Guerry/demo/guerry_bivar.R
/usr/lib64/R/library/Guerry/demo/guerry_density.R
/usr/lib64/R/library/Guerry/demo/guerry_manova.R
/usr/lib64/R/library/Guerry/demo/guerry_mra.R
/usr/lib64/R/library/Guerry/doc/MultiSpat.R
/usr/lib64/R/library/Guerry/doc/MultiSpat.Rmd
/usr/lib64/R/library/Guerry/doc/MultiSpat.html
/usr/lib64/R/library/Guerry/doc/guerry-multivariate.R
/usr/lib64/R/library/Guerry/doc/guerry-multivariate.Rmd
/usr/lib64/R/library/Guerry/doc/guerry-multivariate.html
/usr/lib64/R/library/Guerry/doc/index.html
/usr/lib64/R/library/Guerry/help/AnIndex
/usr/lib64/R/library/Guerry/help/Guerry.rdb
/usr/lib64/R/library/Guerry/help/Guerry.rdx
/usr/lib64/R/library/Guerry/help/aliases.rds
/usr/lib64/R/library/Guerry/help/figures/Guerry-logo.png
/usr/lib64/R/library/Guerry/help/figures/Guerry-vars.png
/usr/lib64/R/library/Guerry/help/figures/README-ex-bivar1-1.png
/usr/lib64/R/library/Guerry/help/figures/README-ex-bivar2-1.png
/usr/lib64/R/library/Guerry/help/figures/README-gfrance1-1.png
/usr/lib64/R/library/Guerry/help/figures/README-gfrance2-1.png
/usr/lib64/R/library/Guerry/help/figures/README-gfrance3-1.png
/usr/lib64/R/library/Guerry/help/figures/README-gfrance4-1.png
/usr/lib64/R/library/Guerry/help/figures/README-gfrance85-labels-1.png
/usr/lib64/R/library/Guerry/help/figures/ex-bivar1.png
/usr/lib64/R/library/Guerry/help/figures/ex-bivar2.png
/usr/lib64/R/library/Guerry/help/paths.rds
/usr/lib64/R/library/Guerry/html/00Index.html
/usr/lib64/R/library/Guerry/html/R.css

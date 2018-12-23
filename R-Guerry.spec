#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Guerry
Version  : 1.6.1
Release  : 4
URL      : https://cran.r-project.org/src/contrib/Guerry_1.6-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Guerry_1.6-1.tar.gz
Summary  : Maps, data and methods related to Guerry (1833) "Moral
Group    : Development/Tools
License  : GPL-2.0
Requires: R-sp
BuildRequires : R-sp
BuildRequires : clr-R-helpers

%description
graphic methods related to Guerry's "Moral Statistics of France". The goal is to facilitate the exploration and
	development of statistical and graphic methods for multivariate data in a geo-spatial context of historical interest.

%prep
%setup -q -c -n Guerry

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530495556

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530495556
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Guerry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Guerry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Guerry
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library Guerry|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Guerry/DESCRIPTION
/usr/lib64/R/library/Guerry/INDEX
/usr/lib64/R/library/Guerry/Meta/Rd.rds
/usr/lib64/R/library/Guerry/Meta/data.rds
/usr/lib64/R/library/Guerry/Meta/features.rds
/usr/lib64/R/library/Guerry/Meta/hsearch.rds
/usr/lib64/R/library/Guerry/Meta/links.rds
/usr/lib64/R/library/Guerry/Meta/nsInfo.rds
/usr/lib64/R/library/Guerry/Meta/package.rds
/usr/lib64/R/library/Guerry/NAMESPACE
/usr/lib64/R/library/Guerry/NEWS
/usr/lib64/R/library/Guerry/data/Rdata.rdb
/usr/lib64/R/library/Guerry/data/Rdata.rds
/usr/lib64/R/library/Guerry/data/Rdata.rdx
/usr/lib64/R/library/Guerry/help/AnIndex
/usr/lib64/R/library/Guerry/help/Guerry.rdb
/usr/lib64/R/library/Guerry/help/Guerry.rdx
/usr/lib64/R/library/Guerry/help/aliases.rds
/usr/lib64/R/library/Guerry/help/paths.rds
/usr/lib64/R/library/Guerry/html/00Index.html
/usr/lib64/R/library/Guerry/html/R.css

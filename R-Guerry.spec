#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Guerry
Version  : 1.7.0
Release  : 25
URL      : https://cran.r-project.org/src/contrib/Guerry_1.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Guerry_1.7.0.tar.gz
Summary  : Maps, Data and Methods Related to Guerry (1833) "Moral
Group    : Development/Tools
License  : GPL-2.0
Requires: R-sp
BuildRequires : R-sp
BuildRequires : buildreq-R

%description
graphic methods related to Guerry's "Moral Statistics of France". The goal is to facilitate the exploration and
	development of statistical and graphic methods for multivariate data in a geo-spatial context of historical interest.

%prep
%setup -q -c -n Guerry
cd %{_builddir}/Guerry

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589520054

%install
export SOURCE_DATE_EPOCH=1589520054
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Guerry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Guerry
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Guerry || :


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

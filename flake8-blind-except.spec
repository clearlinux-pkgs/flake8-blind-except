#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-blind-except
Version  : 0.1.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/ff/f2/ab635e6e420e78c94eab50cd3f53abd3ec27e411793e50b14f29edbb9f0b/flake8-blind-except-0.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/f2/ab635e6e420e78c94eab50cd3f53abd3ec27e411793e50b14f29edbb9f0b/flake8-blind-except-0.1.1.tar.gz
Summary  : A flake8 extension that checks for blind except: statements
Group    : Development/Tools
License  : MIT
Requires: flake8-blind-except-python = %{version}-%{release}
Requires: flake8-blind-except-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
===================

%package python
Summary: python components for the flake8-blind-except package.
Group: Default
Requires: flake8-blind-except-python3 = %{version}-%{release}

%description python
python components for the flake8-blind-except package.


%package python3
Summary: python3 components for the flake8-blind-except package.
Group: Default
Requires: python3-core
Provides: pypi(flake8_blind_except)
Requires: pypi(setuptools)

%description python3
python3 components for the flake8-blind-except package.


%prep
%setup -q -n flake8-blind-except-0.1.1
cd %{_builddir}/flake8-blind-except-0.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583534085
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

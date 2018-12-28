#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-blind-except
Version  : 0.1.1
Release  : 4
URL      : https://files.pythonhosted.org/packages/ff/f2/ab635e6e420e78c94eab50cd3f53abd3ec27e411793e50b14f29edbb9f0b/flake8-blind-except-0.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/f2/ab635e6e420e78c94eab50cd3f53abd3ec27e411793e50b14f29edbb9f0b/flake8-blind-except-0.1.1.tar.gz
Summary  : A flake8 extension that checks for blind except: statements
Group    : Development/Tools
License  : MIT
Requires: flake8-blind-except-python3
Requires: flake8-blind-except-python
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
===================

%package python
Summary: python components for the flake8-blind-except package.
Group: Default
Requires: flake8-blind-except-python3

%description python
python components for the flake8-blind-except package.


%package python3
Summary: python3 components for the flake8-blind-except package.
Group: Default
Requires: python3-core

%description python3
python3 components for the flake8-blind-except package.


%prep
%setup -q -n flake8-blind-except-0.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533001771
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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

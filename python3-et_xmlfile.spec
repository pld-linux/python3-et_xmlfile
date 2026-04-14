%define		module		et_xmlfile
Summary:	An implementation of lxml.xmlfile for the standard library
Summary(pl.UTF-8):	Implementacja lxml.xmlfile dla biblioteki standardowej
Name:		python3-%{module}
Version:	2.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/et-xmlfile/
Source0:	https://files.pythonhosted.org/packages/source/e/et_xmlfile/%{module}-%{version}.tar.gz
# Source0-md5:	d7db773c110c5534e61f288fdfcad807
URL:		https://pypi.org/project/et-xmlfile/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

%description -l pl.UTF-8
et_xmlfile to używająca mało pamięci biblioteka do zapisu dużych
plików XML.

Jest oparta na module xmlfile z lxml z myślą o umożliwieniu tworzenia
kodu działającego w obu bibliotekach. Początkowo powstała dla projektu
openpyxl, ale obecnie jest samodzielnym modułem.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt LICENCE.python LICENCE.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

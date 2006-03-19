%define 	zope_subname	CookieCrumbler
Summary:	Zope product that enables cookie-based authentication
Summary(pl):	Dodatek do Zope umo¿liwiaj±cy uwierzytelnianie przez cookies
Name:		Zope-%{zope_subname}
Version:	1.2
Release:	2
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://hathawaymix.org/Software/%{zope_subname}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	7dbb67adaa6ce552456d8817da4b15d8
URL:		http://hathawaymix.org/Software/CookieCrumbler/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CookieCrumbler is Zope product that enables cookie-based
authentication.

%description -l pl
CookieCrumbler jest dodatkiem do Zope umo¿liwiaj±cym uwierzytelnianie
przez cookies.

%prep
%setup -q -n %{zope_subname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af {dtml,tests,*.py,*.gif,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%{_datadir}/%{name}

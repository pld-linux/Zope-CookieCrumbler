%include        /usr/lib/rpm/macros.python
%define 	zope_subname	CookieCrumbler
Summary:	CookieCrumbler - Zope product that enables cookie-based authentication
Summary(pl):	CookieCrumbler - dodatek do Zope umo¿liwiaj±cy autentykacjê przez cookies
Name:		Zope-%{zope_subname}
Version:	1.1
Release:	1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://hathaway.freezope.org/Software/%{zope_subname}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	427421815e94601c04c87326fc6819c1
URL:		http://hathaway.freezope.org/Software/%{zope_subname}
%pyrequires_eq  python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         product_dir     /usr/lib/zope/Products

%description
CookieCrumbler is Zope product that enables cookie-based
authentication.

%description -l pl
CookieCrumbler jest dodatkiem do Zope umo¿liwiaj±cym autentykacjê
przez cookies.

%prep
%setup -q -n %{zope_subname}

%build
mkdir docs
mv -f {CHANGES.txt,README.txt} docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
        /etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
        /etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc docs/*
%{product_dir}/%{zope_subname}

%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	AuthCookie
Summary:	%{pdir}::%{pnam} perl module 
Summary(cs):	Modul %{pdir}::%{pnam} pro Perl
Summary(da):	Perlmodul %{pdir}::%{pnam}
Summary(de):	%{pdir}::%{pnam} Perl Modul
Summary(es):	Módulo de Perl %{pdir}::%{pnam}
Summary(fr):	Module Perl %{pdir}::%{pnam}
Summary(it):	Modulo di Perl %{pdir}::%{pnam}
Summary(ja):	%{pdir}::%{pnam} Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	%{pdir}::%{pnam} ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul %{pdir}::%{pnam}
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Summary(pt_BR):	Módulo Perl %{pdir}::%{pnam}
Summary(pt):	Módulo de Perl %{pdir}::%{pnam}
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(sv):	%{pdir}::%{pnam} Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(zh_CN):	%{pdir}::%{pnam} Perl Ä£¿é
Name:		perl-%{pdir}-%{pnam}
Version:	3.01
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	mod_perl >= 1.24
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::AuthCookie allows you to intercept a user's first unauthenticated
access to a protected document.  The user will be presented with a custom
form where they can enter authentication credentials.  The credentials
are posted to the server where AuthCookie verifies them and returns a
session key.

%description -l pl
Apache::AuthCookie pozwala na przechwycenie pierwszego nieautoryzowanego
zapytania u¿ytkownika o chroniony dokument.  U¿ytkownik zobaczy formularz,
w który bêdzie musia³ wpisaæ wymagane do autoryzacji dane.  Te dane
zostan± wys³ane na serwer, gdzie AuthCookie zweryfikuje je i zwróci
identyfikator sesji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo '!' | perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*

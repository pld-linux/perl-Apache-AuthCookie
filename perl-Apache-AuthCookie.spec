#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	AuthCookie
Summary:	Apache::AuthCookie Perl module
Summary(cs):	Modul Apache::AuthCookie pro Perl
Summary(da):	Perlmodul Apache::AuthCookie
Summary(de):	Apache::AuthCookie Perl Modul
Summary(es):	Módulo de Perl Apache::AuthCookie
Summary(fr):	Module Perl Apache::AuthCookie
Summary(it):	Modulo di Perl Apache::AuthCookie
Summary(ja):	Apache::AuthCookie Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Apache::AuthCookie ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Apache::AuthCookie
Summary(pl):	Modu³ Perla Apache::AuthCookie
Summary(pt_BR):	Módulo Perl Apache::AuthCookie
Summary(pt):	Módulo de Perl Apache::AuthCookie
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Apache::AuthCookie
Summary(sv):	Apache::AuthCookie Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Apache::AuthCookie
Summary(zh_CN):	Apache::AuthCookie Perl Ä£¿é
Name:		perl-Apache-AuthCookie
Version:	3.05
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4288575a1eedb52b2fb774324cd63ec8
BuildRequires:	perl-devel >= 5
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 1.24
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
echo '!' | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# tests require working apache and interactive configuration setting
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Apache/AuthCookie.pm
%{perl_vendorlib}/Apache/AuthCookie
%{_mandir}/man3/*

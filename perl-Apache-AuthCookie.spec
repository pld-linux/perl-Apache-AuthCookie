#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	AuthCookie
Summary:	Apache::AuthCookie Perl module
Summary(cs):	Modul Apache::AuthCookie pro Perl
Summary(da):	Perlmodul Apache::AuthCookie
Summary(de):	Apache::AuthCookie Perl Modul
Summary(es):	M�dulo de Perl Apache::AuthCookie
Summary(fr):	Module Perl Apache::AuthCookie
Summary(it):	Modulo di Perl Apache::AuthCookie
Summary(ja):	Apache::AuthCookie Perl �⥸�塼��
Summary(ko):	Apache::AuthCookie �� ����
Summary(no):	Perlmodul Apache::AuthCookie
Summary(pl):	Modu� Perla Apache::AuthCookie
Summary(pt_BR):	M�dulo Perl Apache::AuthCookie
Summary(pt):	M�dulo de Perl Apache::AuthCookie
Summary(ru):	������ ��� Perl Apache::AuthCookie
Summary(sv):	Apache::AuthCookie Perlmodul
Summary(uk):	������ ��� Perl Apache::AuthCookie
Summary(zh_CN):	Apache::AuthCookie Perl ģ��
Name:		perl-Apache-AuthCookie
Version:	3.04
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
zapytania u�ytkownika o chroniony dokument.  U�ytkownik zobaczy formularz,
w kt�ry b�dzie musia� wpisa� wymagane do autoryzacji dane.  Te dane
zostan� wys�ane na serwer, gdzie AuthCookie zweryfikuje je i zwr�ci
identyfikator sesji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo '!' | perl Makefile.PL
%{__make}
# tests require working apache and interactive configuration setting
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Apache/AuthCookie.pm
%{perl_sitelib}/Apache/AuthCookie
%{_mandir}/man3/*

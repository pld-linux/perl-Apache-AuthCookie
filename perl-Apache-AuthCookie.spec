#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	AuthCookie
Summary:	Apache::AuthCookie - Perl authentication and authorization via cookies
Summary(pl):	Apache::AuthCookie - uwierzytelnianie i autoryzacja w Perlu za pomoc± ,,cookie''
Name:		perl-Apache-AuthCookie
Version:	3.09_01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSCHOUT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	924df2ddb1a6940d292ae4d427e5f3f9
BuildRequires:	apache-mod_perl >= 1.24
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 1.24
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::AuthCookie allows you to intercept a user's first
unauthenticated access to a protected document. The user will be
presented with a custom form where they can enter authentication
credentials. The credentials are posted to the server where AuthCookie
verifies them and returns a session key.

%description -l pl
Apache::AuthCookie pozwala na przechwycenie pierwszego
nieautoryzowanego zapytania u¿ytkownika o chroniony dokument. 
U¿ytkownik zobaczy formularz, w który bêdzie musia³ wpisaæ wymagane do
autoryzacji dane. Te dane zostan± wys³ane na serwer, gdzie AuthCookie
zweryfikuje je i zwróci identyfikator sesji.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Apache2/AuthCookie.pm
%{perl_vendorlib}/Apache2/AuthCookie
%{perl_vendorlib}/Apache/AuthCookie.pm
%{perl_vendorlib}/Apache/AuthCookie
%{_mandir}/man3/*

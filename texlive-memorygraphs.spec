%global tl_name memorygraphs
%global tl_revision 49631

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.1
Release:	%{tl_revision}.1
Summary:	TikZ styles to typeset graphs of program memory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/memorygraphs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memorygraphs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memorygraphs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines some TikZ styles and adds anchors to existing
styles that ease the declaration of "memory graphs". It is intended for
graphs that represent the memory of a computer program during its
execution.


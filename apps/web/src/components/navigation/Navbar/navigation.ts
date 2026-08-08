export interface NavigationItem {
  label: string;
  href: string;
}

export const navigationItems: NavigationItem[] = [
  {
    label: "Home",
    href: "/",
  },
  {
    label: "Features",
    href: "#features",
  },
  {
    label: "Architecture",
    href: "#architecture",
  },
  {
    label: "Documentation",
    href: "#documentation",
  },
];
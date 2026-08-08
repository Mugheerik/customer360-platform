import Container from "@/components/ui/container";
import Button from "@/components/ui/button";

import { navigationItems } from "./navigation";

export default function Navbar() {
  return (
    <header className="border-b border-border bg-background">
      <Container className="flex h-16 items-center justify-between">
        <a
          href="/"
          className="text-lg font-bold tracking-tight text-text"
        >
          Customer360
        </a>

        <nav className="hidden items-center gap-6 md:flex">
          {navigationItems.map((item) => (
            <a
              key={item.label}
              href={item.href}
              className="text-sm font-medium text-text-secondary transition-colors hover:text-text"
            >
              {item.label}
            </a>
          ))}
        </nav>

        <div className="flex items-center gap-3">
          <Button variant="ghost">
            Sign In
          </Button>

          <Button>
            Get Started
          </Button>
        </div>
      </Container>
    </header>
  );
}
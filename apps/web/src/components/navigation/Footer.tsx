import Container from "@/components/ui/container";

export default function Footer() {
  return (
    <footer className="border-t border-border bg-surface">
      <Container className="flex flex-col gap-4 py-8 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <p className="text-sm font-semibold text-text">
            Customer360
          </p>

          <p className="mt-1 text-sm text-text-secondary">
            Intelligent Customer Relationship Platform
          </p>
        </div>

        <p className="text-sm text-text-secondary">
          © {new Date().getFullYear()} Customer360. All rights reserved.
        </p>
      </Container>
    </footer>
  );
}
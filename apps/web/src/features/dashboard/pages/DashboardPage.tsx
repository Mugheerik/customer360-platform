import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { H1, Lead } from "@/components/ui/typography";

export default function DashboardPage() {
  return (
    <Section>
      <Container>
        <H1>Dashboard</H1>

        <Lead className="mt-4">
          Welcome to Customer360.
        </Lead>
      </Container>
    </Section>
  );
}
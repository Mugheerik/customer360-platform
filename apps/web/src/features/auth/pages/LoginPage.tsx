import Container from "@/components/ui/container";
import Section from "@/components/ui/section";

import LoginForm from "../components/LoginForm";

export default function LoginPage() {
  return (
    <Section className="min-h-[calc(100vh-4rem)] bg-surface">
      <Container className="flex min-h-[calc(100vh-4rem)] items-center justify-center">
        <LoginForm />
      </Container>
    </Section>
  );
}
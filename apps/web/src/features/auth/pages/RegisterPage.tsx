import Container from "@/components/ui/container";
import Section from "@/components/ui/section";

import RegisterForm from "../components/RegisterForm";

export default function RegisterPage() {
  return (
    <Section className="min-h-[calc(100vh-4rem)] bg-surface">
      <Container className="flex min-h-[calc(100vh-4rem)] items-center justify-center py-10">
        <RegisterForm />
      </Container>
    </Section>
  );
}

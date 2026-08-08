import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { H1, Lead } from "@/components/ui/typography";
import Button from "@/components/ui/button";

export default function Hero() {
  return (
    <Section className="flex min-h-[80vh] items-center">
      <Container>
        <div className="mx-auto max-w-4xl text-center">
          <H1>Customer360</H1>

          <Lead className="mx-auto mt-6 max-w-2xl">
            Intelligent Customer Relationship Platform
          </Lead>

          <div className="mt-8 flex flex-col justify-center gap-4 sm:flex-row">
            <Button>
              Get Started
            </Button>

            <Button variant="secondary">
              Documentation
            </Button>
          </div>
        </div>
      </Container>
    </Section>
  );
}
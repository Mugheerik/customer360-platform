import Card from "@/components/ui/card";
import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { Body, H2 } from "@/components/ui/typography";

import { architectureItems } from "./architecture.data";

export default function Architecture() {
  return (
    <Section className="bg-background">
      <Container>
        <div className="mx-auto max-w-3xl text-center">
          <H2>Built as an engineering system</H2>

          <Body className="mt-4">
            Customer360 combines modern application development,
            data engineering, analytics, and DevOps practices into
            one evolving platform.
          </Body>
        </div>

        <div className="mt-16 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {architectureItems.map((item) => (
            <Card key={item.name} className="p-6">
              <h3 className="text-lg font-semibold text-text">
                {item.name}
              </h3>

              <p className="mt-3 text-sm leading-6 text-text-secondary">
                {item.description}
              </p>
            </Card>
          ))}
        </div>
      </Container>
    </Section>
  );
}
import Card from "@/components/ui/card";
import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { Body, H2 } from "@/components/ui/typography";

import { homeFeatures } from "./features.data";

export default function Features() {
  return (
    <Section className="bg-surface">
      <Container>
        <div className="mx-auto max-w-3xl text-center">
          <H2>
            Everything you need to manage customer relationships
          </H2>

          <Body className="mt-4">
            Customer360 provides the essential tools for managing
            customers, organizing work, and tracking every interaction.
          </Body>
        </div>

        <div className="mt-16 grid gap-6 md:grid-cols-2">
          {homeFeatures.map((feature) => {
            const Icon = feature.icon;

            return (
              <Card
                key={feature.title}
                className="p-8 transition-shadow hover:shadow-card"
              >
                <div className="mb-6 inline-flex rounded-md bg-background p-3">
                  <Icon className="h-6 w-6 text-text" />
                </div>

                <h3 className="text-xl font-semibold text-text">
                  {feature.title}
                </h3>

                <p className="mt-3 text-text-secondary">
                  {feature.description}
                </p>
              </Card>
            );
          })}
        </div>
      </Container>
    </Section>
  );
}
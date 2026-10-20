import { useNavigate } from "react-router-dom";

import Button from "@/components/ui/button";
import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { Body, H2 } from "@/components/ui/typography";
import { env } from "@/lib/env";
import { useAuthStore } from "@/store/auth.store";

export default function CTA() {
  const navigate = useNavigate();

  const isAuthenticated = useAuthStore(
    (state) => state.isAuthenticated,
  );

  return (
    <Section className="bg-text">
      <Container className="py-16 text-center">
        <H2 className="text-white">
          Start building with Customer360
        </H2>

        <Body className="mx-auto mt-4 max-w-2xl text-white/70">
          Explore the platform, understand the architecture, and
          follow the evolution of Customer360 from application to
          intelligent data system.
        </Body>

        <div className="mt-8 flex flex-col justify-center gap-4 sm:flex-row">
          <Button
            type="button"
            onClick={() =>
              navigate(isAuthenticated ? "/dashboard" : "/register")
            }
          >
            Get Started
          </Button>

          <Button
            type="button"
            variant="ghost"
            className="text-white hover:bg-white/10"
            onClick={() =>
              window.open(env.apiDocsUrl, "_blank", "noopener,noreferrer")
            }
          >
            Documentation
          </Button>
        </div>
      </Container>
    </Section>
  );
}
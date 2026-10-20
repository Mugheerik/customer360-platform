import { useNavigate } from "react-router-dom";

import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { H1, Lead } from "@/components/ui/typography";
import Button from "@/components/ui/button";
import { env } from "@/lib/env";
import { useAuthStore } from "@/store/auth.store";

export default function Hero() {
  const navigate = useNavigate();

  const isAuthenticated = useAuthStore(
    (state) => state.isAuthenticated,
  );

  return (
    <Section className="flex min-h-[80vh] items-center">
      <Container>
        <div className="mx-auto max-w-4xl text-center">
          <H1>Customer360</H1>

          <Lead className="mx-auto mt-6 max-w-2xl">
            Intelligent Customer Relationship Platform
          </Lead>

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
              variant="secondary"
              onClick={() =>
                window.open(env.apiDocsUrl, "_blank", "noopener,noreferrer")
              }
            >
              Documentation
            </Button>
          </div>
        </div>
      </Container>
    </Section>
  );
}
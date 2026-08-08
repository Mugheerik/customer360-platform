import Architecture from "./components/architecture";
import CTA from "./components/cta";
import Features from "./components/features";
import Hero from "./components/Hero";

export default function HomePage() {
  return (
    <>
      <Hero />
      <Features />
      <Architecture />
      <CTA />
    </>
  );
}
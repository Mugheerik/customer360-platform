import type { HTMLAttributes } from "react";

import { cn } from "@/lib/utils";

type TypographyProps = HTMLAttributes<HTMLElement>;

export function H1({
  className,
  ...props
}: TypographyProps) {
  return (
    <h1
      className={cn(
        "text-4xl font-bold tracking-tight text-text sm:text-5xl lg:text-6xl",
        className,
      )}
      {...props}
    />
  );
}

export function H2({
  className,
  ...props
}: TypographyProps) {
  return (
    <h2
      className={cn(
        "text-3xl font-bold tracking-tight text-text sm:text-4xl",
        className,
      )}
      {...props}
    />
  );
}

export function H3({
  className,
  ...props
}: TypographyProps) {
  return (
    <h3
      className={cn(
        "text-2xl font-semibold tracking-tight text-text",
        className,
      )}
      {...props}
    />
  );
}

export function Lead({
  className,
  ...props
}: TypographyProps) {
  return (
    <p
      className={cn(
        "text-lg leading-8 text-text-secondary sm:text-xl",
        className,
      )}
      {...props}
    />
  );
}

export function Body({
  className,
  ...props
}: TypographyProps) {
  return (
    <p
      className={cn(
        "text-base leading-7 text-text-secondary",
        className,
      )}
      {...props}
    />
  );
}

export function Small({
  className,
  ...props
}: TypographyProps) {
  return (
    <p
      className={cn(
        "text-sm leading-6 text-text-secondary",
        className,
      )}
      {...props}
    />
  );
}
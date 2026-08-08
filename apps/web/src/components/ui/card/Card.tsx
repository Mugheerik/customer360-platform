import type { HTMLAttributes } from "react";

import { cn } from "@/lib/utils";

type CardProps = HTMLAttributes<HTMLDivElement>;

export default function Card({
  className,
  children,
  ...props
}: CardProps) {
  return (
    <div
      className={cn(
        "rounded-lg border border-border bg-surface shadow-card",
        className,
      )}
      {...props}
    >
      {children}
    </div>
  );
}

type CardHeaderProps = HTMLAttributes<HTMLDivElement>;

export function CardHeader({
  className,
  children,
  ...props
}: CardHeaderProps) {
  return (
    <div
      className={cn(
        "border-b border-border px-6 py-4",
        className,
      )}
      {...props}
    >
      {children}
    </div>
  );
}

type CardContentProps = HTMLAttributes<HTMLDivElement>;

export function CardContent({
  className,
  children,
  ...props
}: CardContentProps) {
  return (
    <div
      className={cn("p-6", className)}
      {...props}
    >
      {children}
    </div>
  );
}

type CardFooterProps = HTMLAttributes<HTMLDivElement>;

export function CardFooter({
  className,
  children,
  ...props
}: CardFooterProps) {
  return (
    <div
      className={cn(
        "border-t border-border px-6 py-4",
        className,
      )}
      {...props}
    >
      {children}
    </div>
  );
}
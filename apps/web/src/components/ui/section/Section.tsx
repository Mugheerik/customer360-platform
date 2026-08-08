import type { HTMLAttributes } from "react";

import { cn } from "@/lib/utils";

type SectionProps = HTMLAttributes<HTMLElement>;

export default function Section({
  className,
  ...props
}: SectionProps) {
  return (
    <section
      className={cn(
        "w-full py-20 sm:py-24",
        className,
      )}
      {...props}
    />
  );
}
import { Link } from "react-router-dom";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";

import type { Customer } from "../types/customer.types";

type CustomerTableProps = {
  customers: Customer[];
  onDeactivate: (customerId: string) => void;
  onActivate: (customerId: string) => void;
  isDeactivating?: boolean;
};

export default function CustomerTable({
  customers,
  onDeactivate,
  onActivate,
  isDeactivating = false,
}: CustomerTableProps) {
  if (customers.length === 0) {
    return (
      <Card className="p-8 text-center">
        <p className="text-sm text-text-secondary">
          No customers found.
        </p>
      </Card>
    );
  }

  return (
    <Card className="overflow-hidden">
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-border">
          <thead className="bg-surface">
            <tr>
              <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wide text-text-secondary">
                Customer
              </th>

              <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wide text-text-secondary">
                Email
              </th>

              <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wide text-text-secondary">
                Phone
              </th>

              <th className="px-6 py-4 text-left text-xs font-semibold uppercase tracking-wide text-text-secondary">
                Status
              </th>

              <th className="px-6 py-4 text-right text-xs font-semibold uppercase tracking-wide text-text-secondary">
                Actions
              </th>
            </tr>
          </thead>

          <tbody className="divide-y divide-border bg-background">
            {customers.map((customer) => (
              <tr
                key={customer.id}
                className="transition-colors hover:bg-surface"
              >
                <td className="whitespace-nowrap px-6 py-4">
                  <Link
                    to={`/customers/${customer.id}`}
                    className="font-medium text-text hover:text-primary"
                  >
                    {customer.first_name}{" "}
                    {customer.last_name}
                  </Link>
                </td>

                <td className="whitespace-nowrap px-6 py-4 text-sm text-text-secondary">
                  {customer.email}
                </td>

                <td className="whitespace-nowrap px-6 py-4 text-sm text-text-secondary">
                  {customer.phone ?? "—"}
                </td>

                <td className="whitespace-nowrap px-6 py-4">
                  <span
                    className={
                      customer.status ===
                      "active"
                        ? "inline-flex rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700"
                        : "inline-flex rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-600"
                    }
                  >
                    {customer.status}
                  </span>
                </td>

                <td className="whitespace-nowrap px-6 py-4 text-right">
                  {customer.status ===
                  "active" ? (
                    <Button
                      variant="ghost"
                      type="button"
                      disabled={
                        isDeactivating
                      }
                      onClick={() =>
                        onDeactivate(
                          customer.id,
                        )
                      }
                      className="text-danger hover:bg-red-50"
                    >
                      Deactivate
                    </Button>
                  ) : (
                    <Button
                      variant="ghost"
                      type="button"
                      disabled={
                        isDeactivating
                      }
                      onClick={() =>
                        onActivate(
                          customer.id,
                        )
                      }
                      className="text-primary hover:bg-blue-50"
                    >
                      Activate
                    </Button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Card>
  );
}
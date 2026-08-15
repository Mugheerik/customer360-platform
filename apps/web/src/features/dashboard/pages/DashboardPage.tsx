import {
  Activity,
  ArrowRight,
  Building2,
  Users,
  UserPlus,
} from "lucide-react";
import { useQuery } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";
import Container from "@/components/ui/container";
import Section from "@/components/ui/section";
import { Body, H1, Lead } from "@/components/ui/typography";

import { DashboardService } from "../api/dashboard.api";

type StatCardProps = {
  title: string;
  value: string;
  description: string;
  icon: typeof Users;
};

function StatCard({
  title,
  value,
  description,
  icon: Icon,
}: StatCardProps) {
  return (
    <Card className="p-6">
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-sm font-medium text-text-secondary">
            {title}
          </p>

          <p className="mt-2 text-3xl font-semibold tracking-tight text-text">
            {value}
          </p>

          <p className="mt-2 text-sm text-text-secondary">
            {description}
          </p>
        </div>

        <div className="rounded-lg bg-blue-50 p-3">
          <Icon className="h-5 w-5 text-primary" />
        </div>
      </div>
    </Card>
  );
}

function formatActivityAction(action: string): string {
  return action
    .replace(/_/g, " ")
    .replace(/\b\w/g, (character) =>
      character.toUpperCase(),
    );
}

export default function DashboardPage() {
  const navigate = useNavigate();

  const dashboardQuery = useQuery({
    queryKey: ["dashboard", "summary"],
    queryFn: DashboardService.getSummary,
  });

  if (dashboardQuery.isLoading) {
    return (
      <Section>
        <Container>
          <p className="text-sm text-text-secondary">
            Loading dashboard...
          </p>
        </Container>
      </Section>
    );
  }

  if (
    dashboardQuery.isError ||
    !dashboardQuery.data
  ) {
    return (
      <Section>
        <Container>
          <p className="text-sm text-danger">
            Unable to load dashboard.
          </p>

          <Button
            type="button"
            variant="secondary"
            className="mt-4"
            onClick={() =>
              dashboardQuery.refetch()
            }
          >
            Try Again
          </Button>
        </Container>
      </Section>
    );
  }

  const dashboard = dashboardQuery.data;

  return (
    <Section>
      <Container>
        <div>
          <H1>Dashboard</H1>

          <Lead className="mt-3">
            Welcome back to Customer360.
          </Lead>

          <Body className="mt-2 max-w-2xl text-text-secondary">
            Monitor your customer platform, review
            activity, and access the tools you need
            to manage customer relationships.
          </Body>
        </div>

        <div className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <StatCard
            title="Total Customers"
            value={String(
              dashboard.total_customers,
            )}
            description="Customers in the platform"
            icon={Users}
          />

          <StatCard
            title="Active Customers"
            value={String(
              dashboard.active_customers,
            )}
            description="Currently active customers"
            icon={Activity}
          />

          <StatCard
            title="New Customers"
            value={String(
              dashboard.new_customers,
            )}
            description="Added this month"
            icon={UserPlus}
          />

          <StatCard
            title="Organizations"
            value={String(
              dashboard.organizations,
            )}
            description="Organizations in the platform"
            icon={Building2}
          />
        </div>

        <div className="mt-10 grid gap-6 lg:grid-cols-2">
          <Card className="p-8">
            <div>
              <h2 className="text-lg font-semibold text-text">
                Quick Actions
              </h2>

              <p className="mt-2 text-sm text-text-secondary">
                Common actions for managing your
                customer platform.
              </p>
            </div>

            <div className="mt-6 flex flex-wrap gap-3">
              <Button
                type="button"
                onClick={() =>
                  navigate("/customers")
                }
              >
                Add Customer
              </Button>

              <Button
                type="button"
                variant="secondary"
                onClick={() =>
                  navigate("/customers")
                }
              >
                View Customers
              </Button>
            </div>
          </Card>

          <Card className="p-8">
            <div>
              <h2 className="text-lg font-semibold text-text">
                Recent Activity
              </h2>

              <p className="mt-2 text-sm text-text-secondary">
                Latest activity across the customer
                platform.
              </p>
            </div>

            <div className="mt-6">
              {dashboard.recent_activity.length ===
                0 && (
                <div className="rounded-lg border border-border bg-surface p-6">
                  <p className="text-sm font-medium text-text">
                    No recent activity
                  </p>

                  <p className="mt-1 text-sm text-text-secondary">
                    Customer activity will appear
                    here as the platform is used.
                  </p>
                </div>
              )}

              {dashboard.recent_activity.length >
                0 && (
                <div className="space-y-4">
                  {dashboard.recent_activity.map(
                    (activity) => (
                      <div
                        key={activity.id}
                        className="rounded-lg border border-border p-4"
                      >
                        <div className="flex items-start justify-between gap-4">
                          <div>
                            <p className="text-sm font-medium text-text">
                              {formatActivityAction(
                                activity.action,
                              )}
                            </p>

                            <p className="mt-1 text-xs text-text-secondary">
                              {formatActivityAction(
                                activity.entity_type,
                              )}
                            </p>
                          </div>

                          <p className="text-xs text-text-secondary">
                            {new Date(
                              activity.created_at,
                            ).toLocaleString()}
                          </p>
                        </div>
                      </div>
                    ),
                  )}
                </div>
              )}
            </div>
          </Card>
        </div>

        <Card className="mt-10 p-8">
          <div className="flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <h2 className="text-lg font-semibold text-text">
                Customer Management
              </h2>

              <p className="mt-2 max-w-xl text-sm text-text-secondary">
                Manage customer records, review
                customer information, and track
                relationships across the platform.
              </p>
            </div>

            <Button
              type="button"
              variant="secondary"
              onClick={() =>
                navigate("/customers")
              }
            >
              View Customers

              <ArrowRight className="ml-2 h-4 w-4" />
            </Button>
          </div>
        </Card>
      </Container>
    </Section>
  );
}
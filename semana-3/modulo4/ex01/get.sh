aws iam list-attached-role-policies --role-name StudentRoleDay04 > list-attached-role-policies.json

POLICY_ARN=$(jq -r '.AttachedPolicies[0].PolicyArn' list-attached-role-policies.json)
DEFAULT_VERSION_ID=$(aws iam get-policy --policy-arn "$POLICY_ARN" --query "Policy.DefaultVersionId" --output text)

aws iam get-policy --policy-arn $POLICY_ARN > get-policy.json

aws iam get-policy-version --policy-arn "$POLICY_ARN" --version-id "$DEFAULT_VERSION_ID" > get-policy-version.json
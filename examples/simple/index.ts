import * as infoblox from "@pulumi/infoblox";

const random = new infoblox.Random("my-random", { length: 24 });

export const output = random.result;
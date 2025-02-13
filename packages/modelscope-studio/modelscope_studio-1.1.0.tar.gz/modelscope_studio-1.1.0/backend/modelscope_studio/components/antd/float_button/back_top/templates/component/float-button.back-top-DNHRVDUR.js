import { i as le, a as W, r as ce, g as ae, w as k, b as ue } from "./Index-DUGHvhF7.js";
const E = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, re = window.ms_globals.React.useRef, oe = window.ms_globals.React.useState, se = window.ms_globals.React.useEffect, ie = window.ms_globals.React.useMemo, N = window.ms_globals.ReactDOM.createPortal, de = window.ms_globals.internalContext.useContextPropsContext, fe = window.ms_globals.antd.FloatButton;
var me = /\s/;
function pe(e) {
  for (var t = e.length; t-- && me.test(e.charAt(t)); )
    ;
  return t;
}
var _e = /^\s+/;
function he(e) {
  return e && e.slice(0, pe(e) + 1).replace(_e, "");
}
var D = NaN, ge = /^[-+]0x[0-9a-f]+$/i, be = /^0b[01]+$/i, we = /^0o[0-7]+$/i, ye = parseInt;
function U(e) {
  if (typeof e == "number")
    return e;
  if (le(e))
    return D;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = he(e);
  var o = be.test(e);
  return o || we.test(e) ? ye(e.slice(2), o ? 2 : 8) : ge.test(e) ? D : +e;
}
var F = function() {
  return ce.Date.now();
}, Ee = "Expected a function", xe = Math.max, ve = Math.min;
function Ce(e, t, o) {
  var s, i, n, r, l, u, p = 0, g = !1, c = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(Ee);
  t = U(t) || 0, W(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? xe(U(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function m(d) {
    var w = s, R = i;
    return s = i = void 0, p = d, r = e.apply(R, w), r;
  }
  function x(d) {
    return p = d, l = setTimeout(h, t), g ? m(d) : r;
  }
  function f(d) {
    var w = d - u, R = d - p, M = t - w;
    return c ? ve(M, n - R) : M;
  }
  function _(d) {
    var w = d - u, R = d - p;
    return u === void 0 || w >= t || w < 0 || c && R >= n;
  }
  function h() {
    var d = F();
    if (_(d))
      return v(d);
    l = setTimeout(h, f(d));
  }
  function v(d) {
    return l = void 0, b && s ? m(d) : (s = i = void 0, r);
  }
  function C() {
    l !== void 0 && clearTimeout(l), p = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? r : v(F());
  }
  function I() {
    var d = F(), w = _(d);
    if (s = arguments, i = this, u = d, w) {
      if (l === void 0)
        return x(u);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), m(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return I.cancel = C, I.flush = a, I;
}
var Y = {
  exports: {}
}, P = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ie = E, Se = Symbol.for("react.element"), Re = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, ke = Ie.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Oe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Q(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) Te.call(t, s) && !Oe.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Se,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: ke.current
  };
}
P.Fragment = Re;
P.jsx = Q;
P.jsxs = Q;
Y.exports = P;
var y = Y.exports;
const {
  SvelteComponent: Le,
  assign: z,
  binding_callbacks: G,
  check_outros: Pe,
  children: Z,
  claim_element: $,
  claim_space: Fe,
  component_subscribe: H,
  compute_slots: je,
  create_slot: Ne,
  detach: S,
  element: ee,
  empty: K,
  exclude_internal_props: q,
  get_all_dirty_from_scope: We,
  get_slot_changes: Ae,
  group_outros: Be,
  init: Me,
  insert_hydration: O,
  safe_not_equal: De,
  set_custom_element_data: te,
  space: Ue,
  transition_in: L,
  transition_out: A,
  update_slot_base: ze
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ge,
  getContext: He,
  onDestroy: Ke,
  setContext: qe
} = window.__gradio__svelte__internal;
function V(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Ne(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ee("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = $(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = Z(t);
      i && i.l(r), r.forEach(S), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && ze(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? Ae(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : We(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (L(i, n), o = !0);
    },
    o(n) {
      A(i, n), o = !1;
    },
    d(n) {
      n && S(t), i && i.d(n), e[9](null);
    }
  };
}
function Ve(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && V(e)
  );
  return {
    c() {
      t = ee("react-portal-target"), o = Ue(), n && n.c(), s = K(), this.h();
    },
    l(r) {
      t = $(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Z(t).forEach(S), o = Fe(r), n && n.l(r), s = K(), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      O(r, t, l), e[8](t), O(r, o, l), n && n.m(r, l), O(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && L(n, 1)) : (n = V(r), n.c(), L(n, 1), n.m(s.parentNode, s)) : n && (Be(), A(n, 1, 1, () => {
        n = null;
      }), Pe());
    },
    i(r) {
      i || (L(n), i = !0);
    },
    o(r) {
      A(n), i = !1;
    },
    d(r) {
      r && (S(t), S(o), S(s)), e[8](null), n && n.d(r);
    }
  };
}
function J(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Je(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = je(n);
  let {
    svelteInit: u
  } = t;
  const p = k(J(t)), g = k();
  H(e, g, (a) => o(0, s = a));
  const c = k();
  H(e, c, (a) => o(1, i = a));
  const b = [], m = He("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: f,
    subSlotIndex: _
  } = ae() || {}, h = u({
    parent: m,
    props: p,
    target: g,
    slot: c,
    slotKey: x,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(a) {
      b.push(a);
    }
  });
  qe("$$ms-gr-react-wrapper", h), Ge(() => {
    p.set(J(t));
  }), Ke(() => {
    b.forEach((a) => a());
  });
  function v(a) {
    G[a ? "unshift" : "push"](() => {
      s = a, g.set(s);
    });
  }
  function C(a) {
    G[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    o(17, t = z(z({}, t), q(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = q(t), [s, i, g, c, l, u, r, n, v, C];
}
class Xe extends Le {
  constructor(t) {
    super(), Me(this, t, Je, Ve, De, {
      svelteInit: 5
    });
  }
}
const X = window.ms_globals.rerender, j = window.ms_globals.tree;
function Ye(e, t = {}) {
  function o(s) {
    const i = k(), n = new Xe({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? j;
          return u.nodes = [...u.nodes, l], X({
            createPortal: N,
            node: j
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== i), X({
              createPortal: N,
              node: j
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const Qe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ze(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = $e(o, s), t;
  }, {}) : {};
}
function $e(e, t) {
  return typeof t == "number" && !Qe.includes(e) ? t + "px" : t;
}
function B(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = B(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...E.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(N(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = B(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function et(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const T = ne(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = re(), [l, u] = oe([]), {
    forceClone: p
  } = de(), g = p ? !0 : t;
  return se(() => {
    var x;
    if (!r.current || !e)
      return;
    let c = e;
    function b() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), et(n, f), o && f.classList.add(...o.split(" ")), s) {
        const _ = Ze(s);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var C, a, I;
        (C = r.current) != null && C.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: v
        } = B(e);
        c = v, u(h), c.style.display = "contents", b(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const _ = Ce(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", b(), (x = r.current) == null || x.appendChild(c);
    return () => {
      var f, _;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((_ = r.current) == null || _.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, g, o, s, n, i]), E.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function tt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function nt(e, t = !1) {
  try {
    if (ue(e))
      return e;
    if (t && !tt(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function rt(e, t) {
  return ie(() => nt(e, t), [e, t]);
}
const st = Ye(({
  slots: e,
  children: t,
  target: o,
  ...s
}) => {
  var n;
  const i = rt(o);
  return /* @__PURE__ */ y.jsxs(y.Fragment, {
    children: [/* @__PURE__ */ y.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ y.jsx(fe.BackTop, {
      ...s,
      target: i,
      icon: e.icon ? /* @__PURE__ */ y.jsx(T, {
        clone: !0,
        slot: e.icon
      }) : s.icon,
      description: e.description ? /* @__PURE__ */ y.jsx(T, {
        clone: !0,
        slot: e.description
      }) : s.description,
      tooltip: e.tooltip ? /* @__PURE__ */ y.jsx(T, {
        clone: !0,
        slot: e.tooltip
      }) : s.tooltip,
      badge: {
        ...s.badge,
        count: e["badge.count"] ? /* @__PURE__ */ y.jsx(T, {
          slot: e["badge.count"]
        }) : (n = s.badge) == null ? void 0 : n.count
      }
    })]
  });
});
export {
  st as FloatButtonBackTop,
  st as default
};

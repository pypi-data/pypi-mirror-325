import { i as le, a as F, r as ce, g as ae, w as O, b as ue } from "./Index-C84LxTLf.js";
const E = window.ms_globals.React, re = window.ms_globals.React.forwardRef, oe = window.ms_globals.React.useRef, se = window.ms_globals.React.useState, Q = window.ms_globals.React.useEffect, ie = window.ms_globals.React.useMemo, A = window.ms_globals.ReactDOM.createPortal, de = window.ms_globals.internalContext.useContextPropsContext, fe = window.ms_globals.antd.message;
var me = /\s/;
function _e(e) {
  for (var t = e.length; t-- && me.test(e.charAt(t)); )
    ;
  return t;
}
var pe = /^\s+/;
function he(e) {
  return e && e.slice(0, _e(e) + 1).replace(pe, "");
}
var D = NaN, ge = /^[-+]0x[0-9a-f]+$/i, ye = /^0b[01]+$/i, we = /^0o[0-7]+$/i, Ee = parseInt;
function U(e) {
  if (typeof e == "number")
    return e;
  if (le(e))
    return D;
  if (F(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = F(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = he(e);
  var o = ye.test(e);
  return o || we.test(e) ? Ee(e.slice(2), o ? 2 : 8) : ge.test(e) ? D : +e;
}
var P = function() {
  return ce.Date.now();
}, be = "Expected a function", ve = Math.max, xe = Math.min;
function Ce(e, t, o) {
  var i, s, n, r, l, u, _ = 0, p = !1, c = !1, y = !0;
  if (typeof e != "function")
    throw new TypeError(be);
  t = U(t) || 0, F(o) && (p = !!o.leading, c = "maxWait" in o, n = c ? ve(U(o.maxWait) || 0, t) : n, y = "trailing" in o ? !!o.trailing : y);
  function m(d) {
    var w = i, S = s;
    return i = s = void 0, _ = d, r = e.apply(S, w), r;
  }
  function b(d) {
    return _ = d, l = setTimeout(g, t), p ? m(d) : r;
  }
  function f(d) {
    var w = d - u, S = d - _, M = t - w;
    return c ? xe(M, n - S) : M;
  }
  function h(d) {
    var w = d - u, S = d - _;
    return u === void 0 || w >= t || w < 0 || c && S >= n;
  }
  function g() {
    var d = P();
    if (h(d))
      return v(d);
    l = setTimeout(g, f(d));
  }
  function v(d) {
    return l = void 0, y && i ? m(d) : (i = s = void 0, r);
  }
  function x() {
    l !== void 0 && clearTimeout(l), _ = 0, i = u = s = l = void 0;
  }
  function a() {
    return l === void 0 ? r : v(P());
  }
  function C() {
    var d = P(), w = h(d);
    if (i = arguments, s = this, u = d, w) {
      if (l === void 0)
        return b(u);
      if (c)
        return clearTimeout(l), l = setTimeout(g, t), m(u);
    }
    return l === void 0 && (l = setTimeout(g, t)), r;
  }
  return C.cancel = x, C.flush = a, C;
}
var Z = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ie = E, Se = Symbol.for("react.element"), Re = Symbol.for("react.fragment"), Oe = Object.prototype.hasOwnProperty, ke = Ie.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Te = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function V(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Oe.call(t, i) && !Te.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Se,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: ke.current
  };
}
L.Fragment = Re;
L.jsx = V;
L.jsxs = V;
Z.exports = L;
var R = Z.exports;
const {
  SvelteComponent: Le,
  assign: H,
  binding_callbacks: z,
  check_outros: Pe,
  children: $,
  claim_element: ee,
  claim_space: Ne,
  component_subscribe: B,
  compute_slots: Ae,
  create_slot: Fe,
  detach: I,
  element: te,
  empty: G,
  exclude_internal_props: q,
  get_all_dirty_from_scope: We,
  get_slot_changes: je,
  group_outros: Me,
  init: De,
  insert_hydration: k,
  safe_not_equal: Ue,
  set_custom_element_data: ne,
  space: He,
  transition_in: T,
  transition_out: W,
  update_slot_base: ze
} = window.__gradio__svelte__internal, {
  beforeUpdate: Be,
  getContext: Ge,
  onDestroy: qe,
  setContext: Je
} = window.__gradio__svelte__internal;
function J(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Fe(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = te("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = ee(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = $(t);
      s && s.l(r), r.forEach(I), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && ze(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? je(
          i,
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
      o || (T(s, n), o = !0);
    },
    o(n) {
      W(s, n), o = !1;
    },
    d(n) {
      n && I(t), s && s.d(n), e[9](null);
    }
  };
}
function Xe(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && J(e)
  );
  return {
    c() {
      t = te("react-portal-target"), o = He(), n && n.c(), i = G(), this.h();
    },
    l(r) {
      t = ee(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), $(t).forEach(I), o = Ne(r), n && n.l(r), i = G(), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      k(r, t, l), e[8](t), k(r, o, l), n && n.m(r, l), k(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && T(n, 1)) : (n = J(r), n.c(), T(n, 1), n.m(i.parentNode, i)) : n && (Me(), W(n, 1, 1, () => {
        n = null;
      }), Pe());
    },
    i(r) {
      s || (T(n), s = !0);
    },
    o(r) {
      W(n), s = !1;
    },
    d(r) {
      r && (I(t), I(o), I(i)), e[8](null), n && n.d(r);
    }
  };
}
function X(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Ye(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Ae(n);
  let {
    svelteInit: u
  } = t;
  const _ = O(X(t)), p = O();
  B(e, p, (a) => o(0, i = a));
  const c = O();
  B(e, c, (a) => o(1, s = a));
  const y = [], m = Ge("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: f,
    subSlotIndex: h
  } = ae() || {}, g = u({
    parent: m,
    props: _,
    target: p,
    slot: c,
    slotKey: b,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(a) {
      y.push(a);
    }
  });
  Je("$$ms-gr-react-wrapper", g), Be(() => {
    _.set(X(t));
  }), qe(() => {
    y.forEach((a) => a());
  });
  function v(a) {
    z[a ? "unshift" : "push"](() => {
      i = a, p.set(i);
    });
  }
  function x(a) {
    z[a ? "unshift" : "push"](() => {
      s = a, c.set(s);
    });
  }
  return e.$$set = (a) => {
    o(17, t = H(H({}, t), q(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = q(t), [i, s, p, c, l, u, r, n, v, x];
}
class Ke extends Le {
  constructor(t) {
    super(), De(this, t, Ye, Xe, Ue, {
      svelteInit: 5
    });
  }
}
const Y = window.ms_globals.rerender, N = window.ms_globals.tree;
function Qe(e, t = {}) {
  function o(i) {
    const s = O(), n = new Ke({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? N;
          return u.nodes = [...u.nodes, l], Y({
            createPortal: A,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((_) => _.svelteInstance !== s), Y({
              createPortal: A,
              node: N
            });
          }), l;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
const Ze = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ve(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = $e(o, i), t;
  }, {}) : {};
}
function $e(e, t) {
  return typeof t == "number" && !Ze.includes(e) ? t + "px" : t;
}
function j(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = j(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...E.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(A(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = j(n);
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
const K = re(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = oe(), [l, u] = se([]), {
    forceClone: _
  } = de(), p = _ ? !0 : t;
  return Q(() => {
    var b;
    if (!r.current || !e)
      return;
    let c = e;
    function y() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), et(n, f), o && f.classList.add(...o.split(" ")), i) {
        const h = Ve(i);
        Object.keys(h).forEach((g) => {
          f.style[g] = h[g];
        });
      }
    }
    let m = null;
    if (p && window.MutationObserver) {
      let f = function() {
        var x, a, C;
        (x = r.current) != null && x.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: g,
          clonedElement: v
        } = j(e);
        c = v, u(g), c.style.display = "contents", y(), (C = r.current) == null || C.appendChild(c);
      };
      f();
      const h = Ce(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      m = new window.MutationObserver(h), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", y(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, p, o, i, n, s]), E.createElement("react-child", {
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
const st = Qe(({
  slots: e,
  children: t,
  visible: o,
  onVisible: i,
  onClose: s,
  getContainer: n,
  messageKey: r,
  ...l
}) => {
  const u = rt(n), [_, p] = fe.useMessage({
    ...l,
    getContainer: u
  });
  return Q(() => (o ? _.open({
    ...l,
    key: r,
    icon: e.icon ? /* @__PURE__ */ R.jsx(K, {
      slot: e.icon
    }) : l.icon,
    content: e.content ? /* @__PURE__ */ R.jsx(K, {
      slot: e.content
    }) : l.content,
    onClose(...c) {
      i == null || i(!1), s == null || s(...c);
    }
  }) : _.destroy(r), () => {
    _.destroy(r);
  }), [o, r, l.content, l.className, l.duration, l.icon, l.style, l.type]), /* @__PURE__ */ R.jsxs(R.Fragment, {
    children: [/* @__PURE__ */ R.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), p]
  });
});
export {
  st as Message,
  st as default
};
